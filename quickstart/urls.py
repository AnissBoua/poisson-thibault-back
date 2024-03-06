from django.urls import path
from quickstart.views import *

urlpatterns = [
    path('produits/', ProduitList.as_view()),
    path('produit/<int:pk>/', ProduitDetail.as_view()),
]