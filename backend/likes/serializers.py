from rest_framework import serializers
from .models import likes
class likeSerializer(serializers.ModelSerializer):
    class Meta:
        model=likes
        fields=['id','userId','dishId','createdAt','status','likeId']