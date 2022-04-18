from django.urls import path, include
from . import views

urlpatterns = [
    path('upload-services/', views.uploadServices, name='upload-services'),
]
