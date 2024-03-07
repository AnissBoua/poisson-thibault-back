from django.core.management.base import BaseCommand
from django.utils import timezone
from quickstart.models import Transaction

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = [
            {
                "type": "vente",
                "products": [
                    {
                        "nom": "Dorade",
                        "quantite": 3
                    },
                    {
                        "nom": "Anchois",
                        "quantite": 2
                    }
                ],
                "dateValidation": "2024-03-07 16:45:00.070351",
                "total": 41.94
            },
            {
                "type": "achat",
                "products": [
                    {
                        "nom": "Espadon",
                        "quantite": 1
                    },
                    {
                        "nom": "Saumon",
                        "quantite": 4
                    }
                ],
                "dateValidation": "2024-03-07T18:20:00.070351",
                "total": 82.95
            },
            {
                "type": "vente",
                "products": [
                    {
                        "nom": "Truite",
                        "quantite": 2
                    },
                    {
                        "nom": "Bar",
                        "quantite": 1
                    }
                ],
                "dateValidation": "2024-03-07T20:00:00.070351",
                "total": 50.97
            },
            {
                "type": "achat",
                "products": [
                    {
                        "nom": "Maquereau",
                        "quantite": 2
                    },
                    {
                        "nom": "Morue",
                        "quantite": 3
                    }
                ],
                "dateValidation": "2024-03-07T22:10:00.070351",
                "total": 69.92
            },
            {
                "type": "vente",
                "products": [
                    {
                        "nom": "Thon",
                        "quantite": 3
                    },
                    {
                        "nom": "Sole",
                        "quantite": 1
                    }
                ],
                "dateValidation": "2024-03-07T23:55:00.070351",
                "total": 62.95
            },
            {
                "type": "achat",
                "products": [
                    {
                        "nom": "Anchois",
                        "quantite": 1
                    },
                    {
                        "nom": "Espadon",
                        "quantite": 2
                    }
                ],
                "dateValidation": "2024-03-08T02:30:00.070351",
                "total": 41.97
            },
            {
                "type": "vente",
                "products": [
                    {
                        "nom": "Dorade",
                        "quantite": 2
                    },
                    {
                        "nom": "Saumon",
                        "quantite": 3
                    }
                ],
                "dateValidation": "2024-03-08T05:15:00.070351",
                "total": 99.93
            },
            {
                "type": "achat",
                "products": [
                    {
                        "nom": "Maquereau",
                        "quantite": 4
                    },
                    {
                        "nom": "Truite",
                        "quantite": 1
                    }
                ],
                "dateValidation": "2024-03-08T08:20:00.070351",
                "total": 63.45
            },
            {
                "type": "vente",
                "products": [
                    {
                        "nom": "Morue",
                        "quantite": 3
                    },
                    {
                        "nom": "Bar",
                        "quantite": 1
                    }
                ],
                "dateValidation": "2024-03-08T10:00:00.070351",
                "total": 72.95
            },
            {
                "type": "achat",
                "products": [
                    {
                        "nom": "Sole",
                        "quantite": 2
                    },
                    {
                        "nom": "Thon",
                        "quantite": 2
                    }
                ],
                "dateValidation": "2024-03-08T12:40:00.070351",
                "total": 89.96
            },
            {
                "type": "vente",
                "products": [
                    {
                        "nom": "Anchois",
                        "quantite": 3
                    },
                    {
                        "nom": "Espadon",
                        "quantite": 1
                    }
                ],
                "dateValidation": "2024-03-08T15:25:00.070351",
                "total": 74.95
            },
            {
                "type": "achat",
                "products": [
                    {
                        "nom": "Maquereau",
                        "quantite": 3
                    },
                    {
                        "nom": "Dorade",
                        "quantite": 2
                    }
                ],
                "dateValidation": "2024-03-08T18:10:00.070351",
                "total": 74.94
            },
            {
                "type": "vente",
                "products": [
                    {
                        "nom": "Saumon",
                        "quantite": 2
                    },
                    {
                        "nom": "Truite",
                        "quantite": 1
                    }
                ],
                "dateValidation": "2024-03-08T20:45:00.070351",
                "total": 41.47
            },
            {
                "type": "achat",
                "products": [
                    {
                        "nom": "Morue",
                        "quantite": 4
                    },
                    {
                        "nom": "Bar",
                        "quantite": 1
                    }
                ],
                "dateValidation": "2024-03-08T22:30:00.070351",
                "total": 85.91
            },
            {
                "type": "vente",
                "products": [
                    {
                        "nom": "Sole",
                        "quantite": 3
                    },
                    {
                        "nom": "Thon",
                        "quantite": 1
                    }
                ],
                "dateValidation": "2024-03-09T01:15:00.070351",
                "total": 74.96
            },
            {
                "type": "achat",
                "products": [
                    {
                        "nom": "Anchois",
                        "quantite": 2
                    },
                    {
                        "nom": "Espadon",
                        "quantite": 2
                    }
                ],
                "dateValidation": "2024-03-09T03:50:00.070351",
                "total": 59.94
            },
            {
                "type": "vente",
                "products": [
                    {
                        "nom": "Dorade",
                        "quantite": 1
                    },
                    {
                        "nom": "Saumon",
                        "quantite": 2
                    }
                ],
                "dateValidation": "2024-03-09T06:25:00.070351",
                "total": 53.97
            }
        ]


        for transaction in data:
            Transaction.objects.create(
                type=transaction["type"],
                products=transaction["products"],
                dateValidation=timezone.now(),
                total=transaction["total"],
                dateAjout=timezone.now(),
                dateModif=timezone.now()
            )