from django.contrib import admin

from .models import Album
# Register your models here.

class Album_admin(admin.ModelAdmin):
    list_display = [
        'desc',
        'thumbnail',  
        'creation'
    ]

# register 

admin.site.register(Album,Album_admin)
