from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


class RoleAdmin(admin.ModelAdmin):
    fields = ("role_name",)

class CustomUserAdmin(admin.ModelAdmin):
    fields = ("email",)

admin.site.register(Role, RoleAdmin)
admin.site.register(CustomUser, CustomUserAdmin)



