from django.db import models

# Create your models here.
class post(models.Model):
    id=models.AutoField(primary_key=True)
    userId=models.CharField(max_length=20,unique=True)
    dishName=models.CharField(max_length=20)
    dishPhoto= models.ImageField(upload_to='post')
    dishId=models.CharField(max_length=20,unique=True)
    bio=models.CharField(max_length=500)
    cusine=models.CharField(max_length=50)
    createdAt=models.DateTimeField(auto_now_add=True)

