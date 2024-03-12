import json
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from quickstart.models import Produit
from quickstart.serializer.produit import ProduitSerializer
from quickstart.models import Transaction
from quickstart.models import TransactionProduit
from math import ceil
from datetime import datetime

class ProduitEndpoints(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            return self.getOne(request, pk, format)
        if request.GET.get('search') is not None:
            return self.search(request, format)
        return self.getAll(request, format)
    
    def getOne(self, request, pk, format=None):
        produit = Produit.objects.get(pk=pk)
        produit = ProduitSerializer(produit).data
        return Response(produit)
    
    def getAll(self, request, format=None):
        limit = request.GET.get('limit', 10)
        page = request.GET.get('page', 1)
        produits = Produit.objects.select_related('category').all()
        total = produits.count()
        produits = produits[(int(page) - 1) * int(limit):int(page) * int(limit)]
        res = {
            'data': ProduitSerializer(produits, many=True).data,
            'total': total,
            'limit': limit,
            'page': page,
            'last': ceil(total / int(limit))
        }
        return Response(res)
    
    def search(self, request, format=None):
        search = request.GET.get('search')
        produits = Produit.objects.filter(nom__icontains=search)
        
        return Response(produits.values())
    
class ProduitsUpdates(APIView):
    def patch(self, request, format=None):
        data = json.loads(request.body)
        # Reorder data for easy access : [13 => {}, 15 => {}, 14 => {}]
        data = {produit['id']: produit for produit in data}

        ids = list(data.keys())
        produits = Produit.objects.filter(id__in=ids)
        transactions = {}
        for produit in produits:
            produitData = data[produit.id]
            if produitData['prixSolde'] is not None and produitData['prixSolde'] != produit.prixSolde:
                produit.prixSolde = produitData['prixSolde']
                produit.onSale = True

            if 'stockChange' in produitData:
                if (transactions is None or produitData['stockChange'] not in transactions):
                    transactions[produitData['stockChange']] = {}
                    transactions[produitData['stockChange']]['produits'] = []
                    transactions[produitData['stockChange']]['transaction'] = Transaction()
                    transactions[produitData['stockChange']]['transaction'].type = produitData['stockChange']

                transaction_produit = TransactionProduit()
                transaction_produit.prix = produit.prix
                transaction_produit.quantity = abs(produitData['stock'] - produit.stock)
                transaction_produit.prixSolde = produit.prixSolde
                transaction_produit.ca = round(transaction_produit.quantity * (produit.prixSolde if produit.prixSolde is not None else produit.prix), 2)
                transaction_produit.transaction = transactions[produitData['stockChange']]['transaction']
                transaction_produit.produit = produit
                transactions[produitData['stockChange']]['produits'].append(transaction_produit)

                # produitData['stock'] contient la nouvelle valeur du stock
                produit.stock = produitData['stock']

            produit.save()

        for type in transactions:
            transactions[type]['transaction'].total = 0
            transactions[type]['transaction'].dateValidation = datetime.now()
            transactions[type]['transaction'].save()
            for transaction_produit in transactions[type]['produits']:
                transactions[type]['transaction'].total += transaction_produit.ca
                transaction_produit.save()
            # Besoin de sauvegarder 2 fois, la première fois pour avoir l'id de la transaction, la deuxième fois pour avoir le total
            transactions[type]['transaction'].save()

        produits = ProduitSerializer(produits, many=True).data
        return Response(produits)
        