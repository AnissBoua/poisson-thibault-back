from django.urls import path
from quickstart.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from quickstart.view.auth import Register

urlpatterns = [
    path('produits/', ProduitEndpoints.as_view()),
    path('produits/<int:pk>/', ProduitEndpoints.as_view()),
    path('produits/updates/', ProduitsUpdates.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', Register.as_view(), name='register-api'),
    path('produits/poissons/', PoissonList.as_view()),
    path('produits/poissons/<int:pk>/', PoissonDetail.as_view()),
    path('produits/crustaces/', CrustaceList.as_view()),
    path('produits/crustaces/<int:pk>/', CrustaceDetail.as_view()),
    path('produits/fruit-de-mer/', FruitDeMerList.as_view()),
    path('produits/fruit-de-mer/<int:pk>/', FruitDeMerDetail.as_view()),
    path('categories/', CategoryList.as_view()),
]