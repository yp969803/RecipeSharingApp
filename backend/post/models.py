from django.db import models

# Create your models here.
class post(models.Model):
    id=models.AutoField(primary_key=True)
    userId=models.CharField(max_length=20,unique=False)
    dishName=models.CharField(max_length=20)
    dishPhoto= models.ImageField(upload_to='post')
    dishBio=models.CharField(max_length=500)
    dishCuisine=models.CharField(max_length=50)
    dishTime=models.IntegerField(default=0)
    createdAt=models.DateTimeField(auto_now_add=True)

