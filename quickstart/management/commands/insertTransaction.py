from django.core.management.base import BaseCommand
from django.utils import timezone
from quickstart.models import Transaction

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = [
            {
                "type": "achat",
                "products": '{"Fresh swordfish":{"price":10.5,"quantity":2,"priceOnSale":null,"category":1},"Yellowfin tuna steaks":{"price":5.1,"quantity":5,"priceOnSale":null,"category":1}}',
                "total": 50,
            },
            {
                "type": "vente",
                "products": '{"Fresh swordfish":{"price":10.5,"quantity":2,"priceOnSale":null,"category":1},"Yellowfin tuna steaks":{"price":5.1,"quantity":5,"priceOnSale":null,"category":1}}',
                "total": 50,
            }]
        for d in data:
            transaction = Transaction(
                type=d['type'],
                products=d['products'],
                total=d['total'],
                dateAjout=timezone.now(),
                dateModif=timezone.now(),
                dateValidation= timezone.now(),
            )
            transaction.save()