from django.contrib import admin
from .models import Produit
from .models import Category
from .models import User
from .models import Transaction

# Register your models here.
admin.site.register(Produit)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Transaction)