from django.db import models
# from django.contrib.auth.models import User
from accounts.models import User

# Create your models here.
class Service(models.Model):
    service_kr = models.CharField(max_length=100, blank=False, default="디폴트 서비스")
    service_en = models.CharField(max_length=100, blank=False, default="DEFAULT SERVICE")
    logo_img = models.ImageField(null=True, blank=True, upload_to='logo_imgs', default='') ## 디폴트 로고 이미지 필요
    verified = models.BooleanField(default=False)

class Invitation(models.Model):
    TYPE_CHOICES = (
		('초대 코드', 'code'),
        ('초대 링크', 'link'),
    )

    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='invitation', null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invitation', null=False)
    type = models.CharField(max_length=10, blank=False, choices=TYPE_CHOICES)
    invitation = models.CharField(max_length=2000, blank=False, default='DEFAULT INVITATION')
    desc = models.TextField(blank=True)
    totalClicks = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)

class Click(models.Model):
    invitation = models.ForeignKey(Invitation, on_delete=models.CASCADE, related_name='clicks', null=False)
    created_at = models.DateField(auto_now_add=True)
