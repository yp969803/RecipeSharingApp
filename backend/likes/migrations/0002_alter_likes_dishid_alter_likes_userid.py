# Generated by Django 4.2.3 on 2023-07-15 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='dishId',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='likes',
            name='userId',
            field=models.CharField(max_length=20),
        ),
    ]