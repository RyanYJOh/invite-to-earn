from django.contrib import admin
from .models import Service, Invitation, Click, ServiceCategory

# Register your models here.
class MainAdmin(admin.ModelAdmin):
    readonly_fields = ('id'),

admin.site.register(Service, MainAdmin)
admin.site.register(Invitation, MainAdmin)
admin.site.register(Click, MainAdmin)
admin.site.register(ServiceCategory, MainAdmin)