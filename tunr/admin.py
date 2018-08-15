from django.contrib import admin
from .models import Artist, Song
# Register your models here.

# This is allowing us to use these models as an admin
admin.site.register(Artist)
admin.site.register(Song)