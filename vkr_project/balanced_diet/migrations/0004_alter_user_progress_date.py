# Generated by Django 4.1.6 on 2023-02-19 12:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('balanced_diet', '0003_user_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_progress',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]