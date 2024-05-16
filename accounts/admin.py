from django.contrib import admin
from .models import CustomUser

# Register your models here.

# create CustomeAdmin 
class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active')
    

# register  CustomeUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)