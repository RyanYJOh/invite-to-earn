from django.urls import path, include
from . import views
from rest_framework import routers
from .serializers import UserViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('google/login', views.google_login, name='google_login'),
    path('google/callback/', views.google_callback, name='google_callback'),  
    path('google/login/finish/', views.GoogleLogin.as_view(), name='google_login_todjango'),
    path('my-invitations/<int:user_id>', views.getMyInvitations, name='my-invitations'),
]
