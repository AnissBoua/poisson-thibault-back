# Generated by Django 5.0.3 on 2024-03-08 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0004_alter_transactionproduit_prixsolde'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionproduit',
            name='ca',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]