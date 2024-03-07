from django.urls import path
from quickstart.views import *

urlpatterns = [
    path('produits/', ProduitList.as_view()),
    path('produit/<int:pk>/', ProduitDetail.as_view()),
    path('produits/poissons', PoissonList.as_view()),
    path('produits/poisson/<int:pk>/', PoissonDetail.as_view()),
    path('produits/crustaces', CrustaceList.as_view()),
    path('produits/crustace/<int:pk>/', CrustaceDetail.as_view()),
    path('produits/fruitsDeMer', FruitDeMerList.as_view()),
    path('produits/fruitDeMer/<int:pk>/', FruitDeMerDetail.as_view()),
]