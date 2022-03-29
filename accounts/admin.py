from django.contrib import admin
from .models import User, UserProfile

# Register your models here.
class AccountsAdmin(admin.ModelAdmin):
    readonly_fields = ('id'),

admin.site.register(User, AccountsAdmin)
admin.site.register(UserProfile, AccountsAdmin)