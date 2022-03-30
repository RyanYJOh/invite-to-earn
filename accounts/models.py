from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # nickname = models.CharField(max_length=20, blank=False, default="초대 회장")
    # profile_img = models.ImageField(null=True, blank=True, upload_to='profile_imgs', default='profile_imgs/strange_d1jvr5.jpg')
    
    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_profile', null=False)
    nickname = models.CharField(max_length=20, blank=False, default="소중한 방문객")