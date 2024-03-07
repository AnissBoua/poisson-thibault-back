from django.core.management.base import BaseCommand
from django.utils import timezone
from quickstart.models import Transaction

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = [
            {
                "type": "vente",
                "productsJson": "[{\"nom\": \"Dorade\", \"quantite\": 3, \"price\": 12.99, \"priceOnSale\": null}, {\"nom\": \"Anchois\", \"quantite\": 2, \"price\": 6.99, \"priceOnSale\": 5.99}]",
                "dateValidation": "2024-03-07T16:45:00.070351",
                "total": 41.94
            },
            {
                "type": "achat",
                "productsJson": "[{\"nom\": \"Espadon\", \"quantite\": 1, \"price\": 17.99, \"priceOnSale\": null}, {\"nom\": \"Saumon\", \"quantite\": 4, \"price\": 15.99, \"priceOnSale\": 12.99}]",
                "dateValidation": "2024-03-07T18:20:00.070351",
                "total": 82.95
            },
            {
                "type": "vente",
                "productsJson": "[{\"nom\": \"Truite\", \"quantite\": 2, \"price\": 10.49, \"priceOnSale\": null}, {\"nom\": \"Bar\", \"quantite\": 1, \"price\": 20.99, \"priceOnSale\": 18.99}]",
                "dateValidation": "2024-03-07T20:00:00.070351",
                "total": 50.97
            },
            {
                "type": "achat",
                "productsJson": "[{\"nom\": \"Maquereau\", \"quantite\": 2, \"price\": 7.99, \"priceOnSale\": null}, {\"nom\": \"Morue\", \"quantite\": 3, \"price\": 11.99, \"priceOnSale\": 9.99}]",
                "dateValidation": "2024-03-07T22:10:00.070351",
                "total": 69.92
            },
            {
                "type": "vente",
                "productsJson": "[{\"nom\": \"Thon\", \"quantite\": 3, \"price\": 14.99, \"priceOnSale\": null}, {\"nom\": \"Sole\", \"quantite\": 1, \"price\": 18.99, \"priceOnSale\": 16.99}]",
                "dateValidation": "2024-03-07T23:55:00.070351",
                "total": 62.95
            }
        ]




        for transaction in data:
            Transaction.objects.create(
                type=transaction["type"],
                productsJson=transaction["productsJson"],
                dateValidation=timezone.now(),
                total=transaction["total"],
                dateAjout=timezone.now(),
                dateModif=timezone.now()
            )