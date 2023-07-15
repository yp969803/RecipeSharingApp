from django.urls import path,include
from . import views

urlpatterns=[
    path('getProfile/<str:userId>',views.getProfile),
    path('create',views.createProfile),
    path('update',views.updateProfile),
    path('updateProfilePicture',views.updateProfilePicture),


]
