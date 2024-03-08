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
    path('produits/poissons', PoissonList.as_view()),
    path('produits/poisson/<int:pk>/', PoissonDetail.as_view()),
    path('produits/crustaces', CrustaceList.as_view()),
    path('produits/crustace/<int:pk>/', CrustaceDetail.as_view()),
    path('produits/fruitsDeMer', FruitDeMerList.as_view()),
    path('produits/fruitDeMer/<int:pk>/', FruitDeMerDetail.as_view()),
]