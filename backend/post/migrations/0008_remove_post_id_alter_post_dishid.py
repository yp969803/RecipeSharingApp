# Generated by Django 4.2.3 on 2023-07-30 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_post_dishid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='id',
        ),
        migrations.AlterField(
            model_name='post',
            name='dishId',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
