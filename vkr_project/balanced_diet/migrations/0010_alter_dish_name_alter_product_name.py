# Generated by Django 4.1.6 on 2023-03-19 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balanced_diet', '0009_recipe_amountofprod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
