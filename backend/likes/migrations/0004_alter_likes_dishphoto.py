# Generated by Django 4.2.3 on 2023-07-15 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0003_likes_dishphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='dishPhoto',
            field=models.ImageField(max_length=255, upload_to=''),
        ),
    ]
