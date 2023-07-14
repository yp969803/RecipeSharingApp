from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import likeSerializer
from rest_framework import status
from .models import likes
from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def getStatus(request,dishId):
   try: 
     items=likes.objects.filter(dishId=dishId)
  
     item_data=likeSerializer(items,many=True).data
     return Response({'message':item_data},status=status.HTTP_200_OK)
   except Exception as e:
       print(e)
       return Response({'message':'some error occured'},status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def getLikeStatus(request,dishId):
    try:
        userId=request.user.username
        likeId=userId+dishId
        item=likes.objects.filter(likeId=likeId)
        if not item:
            return Response({'message':'false'},status=status.HTTP_200_OK)
        
        item_data=likeSerializer(item).data
        print(item_data)
        response_data={'message':item_data.get('status')}
        return Response(response_data,status=status.HTTP_200_OK)
       
    except Exception as e:
        print(e)
        response_data = {"message":"Some error occured"}
        return Response(response_data,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def onClick(request,dishId):
    try:
        userId=request.user.username
        likeId=userId+dishId
        item=likes.objects.filter(likeId=likeId)
        
        if not item:
            likes.objects.create(userId=userId,dishId=dishId,likeId=likeId,status=True)
            return Response({'message':'true'},status=status.HTTP_200_OK)
        
        item_data=likeSerializer(item).data
        print(item_data)
        prevStatus=item.status
        item.status=not prevStatus
        item.save()
        print(item)
        item_data=likeSerializer(item).data
        print(item_data,'hello')
        response_data={'message':item_data['status']}
        return Response(response_data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({'message':'some error occured'},status=status.HTTP_200_OK)

