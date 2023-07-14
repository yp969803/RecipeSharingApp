from django.urls import path,include
from . import views

urlpatterns=[
    path('getStatus/<str:dishId>',views.getStatus),
    path('getLikeStatus/<str:dishId>',views.getLikeStatus),
    path('onClick/<str:dishId>',views.onClick)
    
    
]