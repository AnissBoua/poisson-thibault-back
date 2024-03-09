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
    
    def getTransactionProduitsBy(startStr, endStr, category=None, Produit=None):
        if(startStr != endStr):
            startStr = datetime.strptime(startStr, "%Y-%m-%d")
            startStr = startStr - timedelta(days=1)
            endStr = datetime.strptime(endStr, "%Y-%m-%d")
            endStr = endStr + timedelta(days=1)
            if category:
                transactionProduits = TransactionProduit.objects.filter(transaction__type="vente",transaction__dateValidation__range=[startStr,endStr], produit__category__nom=category)
            elif Produit:
                transactionProduits = TransactionProduit.objects.filter(transaction__type="vente",transaction__dateValidation__range=[startStr,endStr], produit__nom=Produit)
            else:
                transactionProduits = TransactionProduit.objects.filter(transaction__type="vente", transaction__dateValidation__range=[startStr, endStr])
            return transactionProduits
        else:
            if category:
                transactionProduits = TransactionProduit.objects.filter(transaction__type="vente",transaction__dateValidation__date=startStr, produit__category__nom=category)
            elif Produit:
                transactionProduits = TransactionProduit.objects.filter(transaction__type="vente",transaction__dateValidation__date=startStr, produit__nom=Produit)
            else:
                transactionProduits = TransactionProduit.objects.filter(transaction__type="vente", transaction__dateValidation__date=startStr)
            return transactionProduits