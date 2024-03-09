import pandas as pd
import json
from django.core import serializers
from datetime import datetime, timedelta

from quickstart.model.transactionProduit import TransactionProduit

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
    
    def getTransactionProduitsBy(start_str, end_str, category=None, produit=None, sale=False):
        if start_str != end_str:
            start_date = datetime.strptime(start_str, "%Y-%m-%d") - timedelta(days=1)
            end_date = datetime.strptime(end_str, "%Y-%m-%d") + timedelta(days=1)

            base_query = {
                'transaction__type': "vente",
                'transaction__dateValidation__range': [start_date, end_date],
            }

            if category:
                base_query['produit__category__nom'] = category
            elif produit:
                base_query['produit__nom'] = produit
            if sale:
                base_query['prixSolde__isnull'] = False
            transaction_produits = TransactionProduit.objects.filter(**base_query)
        else:
            base_query = {
                'transaction__type': "vente",
                'transaction__dateValidation__date': start_str,
            }

            if category:
                base_query['produit__category__nom'] = category
            elif produit:
                base_query['produit__nom'] = produit
            if sale:
                base_query['prixSolde__isnull'] = False
                
            transaction_produits = TransactionProduit.objects.filter(**base_query)
        
        return transaction_produits