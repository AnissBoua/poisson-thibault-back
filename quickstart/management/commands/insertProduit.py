from django.core.management.base import BaseCommand
from django.utils import timezone
from quickstart.models import Produit, Category

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        data = [
            {
                "nom": "Saumon",
                "prix": 15.99,
                "prixSolde": 12.99,
                "stock": 50,
                "commentaire": "Fresh Atlantic salmon fillets",
                "onSale": True
            },
            {
                "nom": "Truite",
                "prix": 10.49,
                "prixSolde": 8.99,
                "stock": 40,
                "commentaire": "Rainbow trout from local rivers",
                "onSale": False
            },
            {
                "nom": "Sole",
                "prix": 18.99,
                "prixSolde": None,
                "stock": 30,
                "commentaire": "Dover sole from the English Channel",
                "onSale": False
            },
            {
                "nom": "Maquereau",
                "prix": 7.99,
                "prixSolde": None,
                "stock": 60,
                "commentaire": "Fresh mackerel caught off the coast",
                "onSale": True
            },
            {
                "nom": "Dorade",
                "prix": 12.99,
                "prixSolde": None,
                "stock": 25,
                "commentaire": "Mediterranean sea bream",
                "onSale": False
            },
            {
                "nom": "Morue",
                "prix": 11.99,
                "prixSolde": None,
                "stock": 35,
                "commentaire": "Atlantic cod for traditional fish and chips",
                "onSale": True
            },
            {
                "nom": "Bar",
                "prix": 20.99,
                "prixSolde": None,
                "stock": 45,
                "commentaire": "Wild sea bass from Brittany",
                "onSale": False
            },
            {
                "nom": "Anchois",
                "prix": 6.99,
                "prixSolde": None,
                "stock": 20,
                "commentaire": "Mediterranean anchovies",
                "onSale": False
            },
            {
                "nom": "Thon",
                "prix": 14.99,
                "prixSolde": None,
                "stock": 55,
                "commentaire": "Yellowfin tuna steaks",
                "onSale": True
            },
            {
                "nom": "Espadon",
                "prix": 17.99,
                "prixSolde": None,
                "stock": 15,
                "commentaire": "Fresh swordfish",
                "onSale": False
            }
        ]
        
        category = Category.objects.get(id=1)
        for produit in data:
            Produit.objects.create(
                nom=produit["nom"],
                prix=produit["prix"],
                prixSolde=produit["prixSolde"],
                stock=produit["stock"],
                commentaire=produit["commentaire"],
                onSale=produit["onSale"],
                dateAjout=timezone.now(),
                dateModif=timezone.now(),
                category=category
            )

        data = [
            {
                "nom": "Crevettes",
                "prix": 15.99,
                "prixSolde": 12.99,
                "stock": 50,
                "commentaire": "Crevettes fraîches de la côte atlantique",
                "onSale": True
            },
            {
                "nom": "Huîtres",
                "prix": 10.49,
                "prixSolde": 8.99,
                "stock": 40,
                "commentaire": "Huîtres spéciales de Bretagne",
                "onSale": False
            },
            {
                "nom": "Coquilles Saint-Jacques",
                "prix": 18.99,
                "prixSolde": None,
                "stock": 30,
                "commentaire": "Délicieuses coquilles Saint-Jacques fraîches",
                "onSale": False
            },
            {
                "nom": "Moules",
                "prix": 7.99,
                "prixSolde": None,
                "stock": 60,
                "commentaire": "Moules fraîches de la baie de Mont-Saint-Michel",
                "onSale": True
            },
            {
                "nom": "Langoustines",
                "prix": 12.99,
                "prixSolde": None,
                "stock": 25,
                "commentaire": "Langoustines fraîches pêchées au large",
                "onSale": False
            },
            {
                "nom": "Palourdes",
                "prix": 11.99,
                "prixSolde": None,
                "stock": 35,
                "commentaire": "Palourdes fraîches de Normandie",
                "onSale": True
            },
            {
                "nom": "Bigorneaux",
                "prix": 20.99,
                "prixSolde": None,
                "stock": 45,
                "commentaire": "Bigorneaux fraîchement pêchés sur la côte",
                "onSale": False
            },
            {
                "nom": "Crabes",
                "prix": 6.99,
                "prixSolde": None,
                "stock": 20,
                "commentaire": "Crabes frais de l'océan Atlantique",
                "onSale": False
            },
            {
                "nom": "Homards",
                "prix": 14.99,
                "prixSolde": None,
                "stock": 55,
                "commentaire": "Homards fraîchement pêchés dans les eaux côtières",
                "onSale": True
            },
            {
                "nom": "Saint-Pierre",
                "prix": 17.99,
                "prixSolde": None,
                "stock": 15,
                "commentaire": "Saint-Pierre sauvage de la Manche",
                "onSale": False
            }
        ]

        category = Category.objects.get(id=2)
        for produit in data:
            Produit.objects.create(
                nom=produit["nom"],
                prix=produit["prix"],
                prixSolde=produit["prixSolde"],
                stock=produit["stock"],
                commentaire=produit["commentaire"],
                onSale=produit["onSale"],
                dateAjout=timezone.now(),
                dateModif=timezone.now(),
                category=category
            )
        
        data = [
            {
                "nom": "Crevettes géantes",
                "prix": 15.99,
                "prixSolde": 12.99,
                "stock": 50,
                "commentaire": "Crevettes géantes fraîches de la mer du Nord",
                "onSale": True
            },
            {
                "nom": "Homard breton",
                "prix": 10.49,
                "prixSolde": 8.99,
                "stock": 40,
                "commentaire": "Homard breton de qualité supérieure",
                "onSale": False
            },
            {
                "nom": "Crabe des neiges",
                "prix": 18.99,
                "prixSolde": None,
                "stock": 30,
                "commentaire": "Crabe des neiges frais pêché dans les eaux froides",
                "onSale": False
            },
            {
                "nom": "Langoustines",
                "prix": 7.99,
                "prixSolde": None,
                "stock": 60,
                "commentaire": "Langoustines fraîches de la côte bretonne",
                "onSale": True
            },
            {
                "nom": "Écrevisses",
                "prix": 12.99,
                "prixSolde": None,
                "stock": 25,
                "commentaire": "Écrevisses fraîches de rivière",
                "onSale": False
            },
            {
                "nom": "Crevettes roses",
                "prix": 11.99,
                "prixSolde": None,
                "stock": 35,
                "commentaire": "Crevettes roses fraîches de Méditerranée",
                "onSale": True
            },
            {
                "nom": "Tourteau",
                "prix": 20.99,
                "prixSolde": None,
                "stock": 45,
                "commentaire": "Tourteau fraîchement pêché sur les côtes",
                "onSale": False
            },
            {
                "nom": "Crabe royal",
                "prix": 6.99,
                "prixSolde": None,
                "stock": 20,
                "commentaire": "Crabe royal des eaux froides de l'océan Pacifique",
                "onSale": False
            },
            {
                "nom": "Crevettes tigrées",
                "prix": 14.99,
                "prixSolde": None,
                "stock": 55,
                "commentaire": "Crevettes tigrées géantes de l'Asie du Sud-Est",
                "onSale": True
            },
            {
                "nom": "Homard européen",
                "prix": 17.99,
                "prixSolde": None,
                "stock": 15,
                "commentaire": "Homard européen de la Manche",
                "onSale": False
            }
        ]

        category = Category.objects.get(id=3)
        for produit in data:
            Produit.objects.create(
                nom=produit["nom"],
                prix=produit["prix"],
                prixSolde=produit["prixSolde"],
                stock=produit["stock"],
                commentaire=produit["commentaire"],
                onSale=produit["onSale"],
                dateAjout=timezone.now(),
                dateModif=timezone.now(),
                category=category
            )
