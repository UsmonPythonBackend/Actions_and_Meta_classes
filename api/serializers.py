# Web Application
# Telegram API
from rest_framework import serializers
from api.models import Artist, Albom, Songs, SongsAlbom


# Web
class ArtistSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'first_name', 'last_name', 'nick_name', 'image', 'listen', 'status')

class AlbomSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = ('id','title', 'artist', 'description', 'listen', 'status')

class SongsSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('id', 'title', 'artis', 'description', 'listen', 'status')

class SongsAlbomSerializerWeb(serializers.ModelSerializer):
    class Meta:
        model = SongsAlbom
        fields = ('id', 'artist', 'songs', 'status')

#Telegram
class ArtistSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('first_name', 'last_name', 'nick_name', 'image', 'listen', 'status')

class AlbomSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Albom
        fields = ('title', 'description', 'listen', 'status')

class SongsSerializerTelegram(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('title', 'artis', 'description', 'listen', 'status')

