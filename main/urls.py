from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('create', views.postInvitation, name='post-invitation'),
    path('create-service', views.postService, name='post-service'),
    path('clicks', views.postClick, name='clicks'),
    path('get-invitation/<int:service_id>', views.getRandomInvitation, name='get-random-invitation'),
    path('search-invitation/<str:keyword>', views.searchInvitation, name='search-invitation'),
    path('search-service/<str:keyword>', views.searchService, name='search-service'),
    path('all-services', views.getAllServices, name='all-services'),
]
