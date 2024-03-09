from django.core.management.base import BaseCommand
from django.utils import timezone
from quickstart.models import TransactionProduit

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = [
            {
                "prix": 5,
                "prixSolde": None,
                "quantity": 3,
                "transaction": 1,
                "produit": 1
            },
            {
                "prix": 2.2,
                "prixSolde": None,
                "quantity": 1,
                "transaction": 2,
                "produit": 3
            },
            {
                "prix": 40,
                "prixSolde": 20,
                "quantity": 1,
                "transaction": 3,
                "produit": 4
            },
            {
                "prix": 12.99,
                "prixSolde": None,
                "quantity": 10,
                "transaction": 2,
                "produit": 5
            }
        ]




        for transaction in data:
            ca = 0
            if transaction["prix"]:
                ca = transaction["prix"]*transaction["quantity"]
            else:
                ca = transaction["prixSolde"]*transaction["quantity"]
            TransactionProduit.objects.create(
                prix=transaction["prix"],
                prixSolde=transaction["prixSolde"],
                quantity=transaction["quantity"],
                transaction_id=transaction["transaction"],
                produit_id=transaction["produit"],
                ca=ca
            )