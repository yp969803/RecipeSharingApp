# Generated by Django 4.2.3 on 2023-07-13 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userId', models.CharField(max_length=20)),
                ('profilePhoto', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=20)),
                ('bio', models.CharField(max_length=500)),
                ('emailId', models.CharField(max_length=50)),
            ],
        ),
    ]
