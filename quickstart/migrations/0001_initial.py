# Generated by Django 5.0.3 on 2024-03-05 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=100)),
                ('dateAjout', models.DateTimeField(auto_now_add=True)),
                ('dateModif', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('vente', 'Vente'), ('achat', 'Achat')], default='vente', max_length=100)),
                ('products', models.TextField()),
                ('dateValidation', models.DateTimeField()),
                ('total', models.FloatField()),
                ('dateAjout', models.DateTimeField(auto_now_add=True)),
                ('dateModif', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('dateAjout', models.DateTimeField(auto_now_add=True)),
                ('dateModif', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('prix', models.FloatField()),
                ('prixSolde', models.FloatField()),
                ('stock', models.IntegerField()),
                ('commentaire', models.TextField()),
                ('onSale', models.BooleanField(default=False)),
                ('dateAjout', models.DateTimeField(auto_now_add=True)),
                ('dateModif', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.category')),
            ],
        ),
    ]
