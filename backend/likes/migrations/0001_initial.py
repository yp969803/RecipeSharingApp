# Generated by Django 4.2.3 on 2023-07-14 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userId', models.CharField(max_length=20, unique=True)),
                ('dishId', models.CharField(max_length=20, unique=True)),
                ('likeId', models.CharField(max_length=50, unique=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
