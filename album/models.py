from django.db import models

# Create your models here.

class Album(models.Model):
    thumbnail = models.ImageField(upload_to= 'album/photo/')
    desc = models.TextField()
    creation = models.DateField( auto_now_add= True)