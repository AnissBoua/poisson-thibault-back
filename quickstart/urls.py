from django.urls import path
from quickstart.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from quickstart.view.auth import Register

urlpatterns = [
    path('produits/', ProduitList.as_view()),
    path('produit/<int:pk>/', ProduitDetail.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', Register.as_view(), name='register-api'),
]