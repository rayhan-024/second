from django.contrib import admin

from .models import Profile
# Register your models here.

class Profile_admin(admin.ModelAdmin):
    list_display = [
        'name',
        'age',
        'address',
        'image'
    ]

# register 

admin.site.register(Profile, Profile_admin)