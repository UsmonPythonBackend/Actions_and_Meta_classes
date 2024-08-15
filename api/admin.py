from django.contrib import admin

from .models import Albom, Artist, SongsAlbom, Songs

admin.site.register([Albom, Artist, SongsAlbom, Songs])
