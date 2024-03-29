import pandas as pd
import json
from django.core import serializers
from datetime import datetime, timedelta

from quickstart.model.transactionProduit import TransactionProduit
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from calendar import monthrange

class CAService():
    def getDateRange(startStr, endStr):
        start = pd.to_datetime(startStr)
        end = pd.to_datetime(endStr)

        dates = pd.date_range(start, end)
        date_strings = [date.strftime('%Y-%m-%d') for date in dates]
        return date_strings
    
    def getCA(transactionProduits, startStr, endStr):
        dateRange = CAService.getDateRange(startStr, endStr)
        cas = []
        map = {}
        for date in dateRange:
            map[date] = []

        for transactionProduit in transactionProduits:
            date = transactionProduit.transaction.dateValidation.date().strftime("%Y-%m-%d")
            if date in map:
                map[date].append(transactionProduit)
            else:
                map[date] = [transactionProduit]
        
        for elem in map:
            ca = {
                "date": elem,
                "ca": 0
            }
            for transactionProduit in map[elem]:
                ca["ca"] += transactionProduit.ca
            
            cas.append(ca)

        return cas
    
    def getTransactionProduitsBy(start_str, end_str, category=None, produit=None, sale=False ,type="vente"):
        if start_str != end_str:
            start_date = datetime.strptime(start_str, "%Y-%m-%d") - timedelta(days=1)
            end_date = datetime.strptime(end_str, "%Y-%m-%d") + timedelta(days=1)

            base_query = {
                'transaction__type': type,
                'transaction__dateValidation__range': [start_date, end_date],
            }

            if category:
                base_query['produit__category__id'] = category
            elif produit:
                base_query['produit__id'] = produit
            if sale:
                base_query['prixSolde__isnull'] = False
            transaction_produits = TransactionProduit.objects.filter(**base_query)
        else:
            base_query = {
                'transaction__type': "vente",
                'transaction__dateValidation__date': start_str,
            }

            if category:
                base_query['produit__category__id'] = category
            elif produit:
                base_query['produit__id'] = produit
            if sale:
                base_query['prixSolde__isnull'] = False
                
            transaction_produits = TransactionProduit.objects.filter(**base_query)
        
        return transaction_produits
    
    def getThisMounthCA():
        start = datetime.now().replace(day=1)
        end = datetime.now()
        start_str = start.strftime("%Y-%m-%d")
        end_str = end.strftime("%Y-%m-%d")
        print(start, end)
        transactionProduits = CAService.getTransactionProduitsBy(start_str=start_str, end_str=end_str)
        print(transactionProduits)
        cas = CAService.getCA(transactionProduits, start, end)
        mounth_ca = CAService.getCaNumber(cas)
        channel_layer = get_channel_layer()
        message = {'type': 'new_ca', 'content': mounth_ca}
        async_to_sync(channel_layer.group_send)("ca_group", {"type": "send_message", "message": json.dumps(message)})
        return mounth_ca
    
    def getYearlyInvoice(year):
        start = datetime(year, 1, 1)
        end = datetime(year, 12, 31)
        start_str = start.strftime("%Y-%m-%d")
        end_str = end.strftime("%Y-%m-%d")
        transactionProduits = CAService.getTransactionProduitsBy(start_str=start_str, end_str=end_str, type="achat")
        cas = CAService.getCA(transactionProduits, start, end)
        year_invoice = CAService.getCaNumber(cas)
        return year_invoice
    
    def getYearlyCa(year):
        start = datetime(year, 1, 1)
        end = datetime(year, 12, 31)
        start_str = start.strftime("%Y-%m-%d")
        end_str = end.strftime("%Y-%m-%d")
        transactionProduits = CAService.getTransactionProduitsBy(start_str=start_str, end_str=end_str)
        cas = CAService.getCA(transactionProduits, start, end)
        year_ca = CAService.getCaNumber(cas)
        return year_ca
    
    def getYearlyMargin(year):
        yearly_invoice = CAService.getYearlyInvoice(year)
        yearly_ca = CAService.getYearlyCa(year)

        return yearly_ca - yearly_invoice
    
    def getTrimesterInvoice(year, trimester):
        start = datetime(year, (trimester-1)*3+1, 1)
        _,last_day = monthrange(year, trimester*3)
        end = datetime(year, trimester*3, last_day)
        start_str = start.strftime("%Y-%m-%d")
        end_str = end.strftime("%Y-%m-%d")
        transactionProduits = CAService.getTransactionProduitsBy(start_str=start_str, end_str=end_str, type="achat")
        cas = CAService.getCA(transactionProduits, start, end)
        trimester_invoice = CAService.getCaNumber(cas)
        return trimester_invoice
    
    def getTrimesterCa(year, trimester):
        start = datetime(year, (trimester-1)*3+1, 1)
        _,last_day = monthrange(year, trimester*3)
        end = datetime(year, trimester*3, last_day)
        start_str = start.strftime("%Y-%m-%d")
        end_str = end.strftime("%Y-%m-%d")
        transactionProduits = CAService.getTransactionProduitsBy(start_str=start_str, end_str=end_str)
        cas = CAService.getCA(transactionProduits, start, end)
        trimester_ca = CAService.getCaNumber(cas)
        return trimester_ca
    
    def getTrimesterMargin(year, trimester):
        trimester_invoice = CAService.getTrimesterInvoice(year, trimester)
        trimester_ca = CAService.getTrimesterCa(year, trimester)
        return trimester_ca - trimester_invoice
    
    def getAverageMarginLasts6Trimesters(year, trimester):
        margin = 0
        trimester -= 1
        if (trimester == 0):
            trimester = 4
            year -= 1 

        for i in range(1, 6):
            margin += CAService.getTrimesterMargin(year, trimester)
            if (trimester == 1):
                trimester = 5
                year -= 1 
            trimester -= 1
        return margin / 6
    
    def getYearlyCategoryRepartition(year):
        start = datetime(year, 1, 1)
        end = datetime(year, 12, 31)
        start_str = start.strftime("%Y-%m-%d")
        end_str = end.strftime("%Y-%m-%d")
        transactionProduits = CAService.getTransactionProduitsBy(start_str=start_str, end_str=end_str)
        cas = CAService.getCA(transactionProduits, start, end)
        categoryRepartition = {}
        for elem in cas:
            date = elem['date']
            for transactionProduit in transactionProduits:
                if transactionProduit.transaction.dateValidation.date().strftime("%Y-%m-%d") == date:
                    category = transactionProduit.produit.category.nom
                    if category in categoryRepartition:
                        categoryRepartition[category] += transactionProduit.ca
                    else:
                        categoryRepartition[category] = transactionProduit.ca
        return categoryRepartition
    
    def getCaNumber(cas):
        ca = 0
        for elem in cas:
            ca += elem['ca']
        return ca