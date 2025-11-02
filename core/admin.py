from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(SYMPTOMS)
class symptomsAdmin(admin.ModelAdmin):
    list_display = ['id','name']






@admin.register(DESEASE)
class diseaseAdmin(admin.ModelAdmin):
    list_display = ['id','name']
    


@admin.register(USER)
class CustomUserAdmin(UserAdmin):
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        
    )



@admin.register(PATIENT)
class symptomsAdmin(admin.ModelAdmin):
    list_display = ('user', 'picture', 'age', 'gender', )