from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import userProfileSerializer
from rest_framework import status
from .models import userProfile
from django.shortcuts import get_object_or_404

from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def getProfile(request,userId):
    user_profile=get_object_or_404(userProfile,userId=userId)
    serializer=userProfileSerializer(instance=user_profile)
    return Response({"user_profile":serializer.data})

@api_view(['POST'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def createProfile(request):
    try:
       userId=request.user.username
       name=request.data['name']
       profilePhoto=request.data['profilePhoto']
       emailId=request.data['emailId']
       bio=request.data['bio']
       userProfile.objects.create(userId=userId,name=name,profilePhoto=profilePhoto,emailId=emailId,bio=bio)
       response_data = {"message":"Profile Saved"}
       return Response(response_data,status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        response_data = {"message":"Some error occured"}
        return Response(response_data,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
@authentication_classes([SessionAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateProfile(request):
    try:
        userId=request.user.username
        name=request.data['name']
        profilePhoto=request.data['profilePhoto']
        emailId=request.data['emailId']
        bio=request.data['bio']
        item=userProfile.objects.filter(userId=userId).first()
        if item is None:
            return Response({'message':'Some error occured'},status=status.HTTP_404_NOT_FOUND)
        item.name=name
        item.profilePhoto=profilePhoto
        item.emailId=emailId
        item.bio=bio
        item.save()
        item_data=userProfileSerializer(item).data
        return Response({'profile':item_data},status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({'message':'some error occured'},status=status.HTTP_200_OK)



