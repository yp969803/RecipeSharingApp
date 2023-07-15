from django.db import models

# Create your models here.
class likes(models.Model):
    id=models.AutoField(primary_key=True)
    userId=models.CharField(max_length=20,unique=False)
    dishId=models.CharField(max_length=20,unique=False)
    likeId=models.CharField(max_length=50,unique=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)


