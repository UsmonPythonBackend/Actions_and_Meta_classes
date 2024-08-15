from requests import Response
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import authentication
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializerWeb, AlbomSerializerWeb, SongsSerializerWeb, ArtistSerializerTelegram, AlbomSerializerTelegram, SongsSerializerTelegram


# Web
class ArtistViewSetWeb(viewsets.ModelViewSet):
    serializer_class = ArtistSerializerWeb
    permission_classes = [IsAuthenticated]
    autehntication_classes = [authentication.TokenAuthentication]


    def get_queryset(self):
        return Artist.objects.filter(status='pb')


    @action(detail=True, methods=["GET", ])
    def listen(self, request, *args, **kwargs):
        artist = self.get_object()
        artist.listen += 1
        artist.save()
        return Response(data={"listened": artist.listen})



    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        artists = self.get_queryset().order_by("-listen")[:3]
        serializer = ArtistSerializerWeb(artists, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



    @action(detail=False, method=["GET", ])
    def null_listen(self, request, *args, **kwargs):
        artists = self.get_queryset().filter(listen=0)
        serializer = ArtistSerializerWeb(artists, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



    @action(detail=False, methods=["GET", ])
    def all_listen(self, request, *args, **kwargs):
        artists = Artist.objects.all()
        for artist in artists:
            artist.listen += 1
            artist.save()
        return Response(data={"message": "all artist music listened"})


    @action(detail=False, method=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        artists = self.get_queryset()  # Songs.objects.all()
        for artist in artists:
            artist.pb_to_df()
        return Response(data={"message": "all data changes to draft"})


    @action(detail=False, method=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        artists = Artist.object.all()
        for artist in artists:
            artist.df_to_pb()
        return Response(data={"message": "all data changes to publish"})


    @action(detail=False, method=["GET", ])
    def to_publish_d(self, request, *args, **kwargs):
        artist = self.get_object()
        artist.df_to_pb()
        return Response(data={"message": "data changes to publish"})

    @action(detail=False, method=["GET", ])
    def to_draft_d(self, request, *args, **kwargs):
        artist = Artist.objects.get(id=id)
        artist.pb_to_df()
        return Response(data={"message": "data changes to draft"})


class AlbomViewSetWeb(viewsets.ModelViewSet):
    serializer_class = AlbomSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    def get_queryset(self):
        return Albom.objects.filter(status='pb')


    @action(detail=True, methods=["GET", ])
    def listen(self, request, *args, **kwargs):
        albom = self.get_object()
        albom.listen += 1
        albom.save()
        return Response(data={"listened": albom.listen})



    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        alboms = self.get_queryset().order_by("-listen")[:3]
        serializer = AlbomSerializerWeb(alboms, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



    @action(detail=False, method=["GET", ])
    def null_listen(self, request, *args, **kwargs):
        alboms = self.get_queryset().filter(listen=0)
        serializer = AlbomSerializerWeb(alboms, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



    @action(detail=False, methods=["GET", ])
    def all_listen(self, request, *args, **kwargs):
        alboms = Albom.objects.all()
        for albom in alboms:
            albom.listen += 1
            albom.save()
        return Response(data={"message": "all albom music listened"})


    @action(detail=False, method=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        alboms = self.get_queryset()  # Songs.objects.all()
        for albom in alboms:
            albom.pb_to_df()
        return Response(data={"message": "all data changes to draft"})


    @action(detail=False, method=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        alboms = Albom.object.all()
        for albom in alboms:
            albom.df_to_pb()
        return Response(data={"message": "all data changes to publish"})


    @action(detail=False, method=["GET", ])
    def to_publish_d(self, request, *args, **kwargs):
        albom = self.get_object()
        albom.df_to_pb()
        return Response(data={"message": "data changes to publish"})

    @action(detail=False, method=["GET", ])
    def to_draft_d(self, request, *args, **kwargs):
        albom = Albom.objects.get(id=id)
        albom.pb_to_df()
        return Response(data={"message": "data changes to draft"})




class SongsViewSetWeb(viewsets.ModelViewSet):
    serializer_class = SongsSerializerWeb
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


    def get_queryset(self):
        return Songs.objects.filter(status='pb')


#Qo'shiqlar eshitilganda listened bittadan qo'shiladi
    @action(detail=True, methods=["GET", ])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        song.listen += 1
        song.save()
        return Response(data={"listened": song.listen})


#Eng ko'p eshitilgan 3ta qo'shiqlar ro'yhati
    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        #1-variant
        songs = self.get_queryset().order_by("-listen")[:3]
        #2-variant
        # songs = self.get_queryset().order_by("listen")[-3::]
        serializer = SongsSerializerWeb(songs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


#Biror marta listen bo'lmagan qo'shiqni chiqarish
    @action(detail=False, method=["GET", ])
    def null_listen(self, request, *args, **kwargs):
        songs = self.get_queryset().filter(listen=0)
        serializer = SongsSerializerWeb(songs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


#Bracha qo'shiqlarga bittadan listen qo'shish
    @action(detail=False, methods=["GET", ])
    def all_listen(self, request, *args, **kwargs):
        songs = Songs.objects.all()
        for song in songs:
            song.listen += 1
            song.save()
        return Response(data={"message": "all music listened"})


    @action(detail=False, method=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        songs = self.get_queryset()  # Songs.objects.all()
        for song in songs:
            song.pb_to_df()
        return Response(data={"message": "all data changes to draft"})


    @action(detail=False, method=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        songs = Songs.object.all()
        for song in songs:
            song.df_to_pb()
        return Response(data={"message": "all data changes to publish"})


    @action(detail=False, method=["GET", ])
    def to_publish_d(self, request, *args, **kwargs):
        song = self.get_object()
        song.df_to_pb()
        return Response(data={"message": "data changes to publish"})

    @action(detail=False, method=["GET", ])
    def to_draft_d(self, request, *args, **kwargs):
        song = Songs.objects.get(id=id)
        song.pb_to_df()
        return Response(data={"message": "data changes to draft"})




# Telegram
class ArtistViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = ArtistSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


    def get_queryset(self):
        return Artist.objects.filter(status='pb')


    @action(detail=True, methods=["GET", ])
    def listen(self, request, *args, **kwargs):
        artist = self.get_object()
        artist.listen += 1
        artist.save()
        return Response(data={"listened": artist.listen})



    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        artists = self.get_queryset().order_by("-listen")[:3]
        serializer = ArtistSerializerTelegram(artists, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



    @action(detail=False, method=["GET", ])
    def null_listen(self, request, *args, **kwargs):
        artists = self.get_queryset().filter(listen=0)
        serializer = ArtistSerializerTelegram(artists, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



    @action(detail=False, methods=["GET", ])
    def all_listen(self, request, *args, **kwargs):
        artists = Artist.objects.all()
        for artist in artists:
            artist.listen += 1
            artist.save()
        return Response(data={"message": "all artist music listened"})


    @action(detail=False, method=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        artists = self.get_queryset()  # Songs.objects.all()
        for artist in artists:
            artist.pb_to_df()
        return Response(data={"message": "all data changes to draft"})


    @action(detail=False, method=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        artists = Artist.object.all()
        for artist in artists:
            artist.df_to_pb()
        return Response(data={"message": "all data changes to publish"})


    @action(detail=False, method=["GET", ])
    def to_publish_d(self, request, *args, **kwargs):
        artist = self.get_object()
        artist.df_to_pb()
        return Response(data={"message": "data changes to publish"})

    @action(detail=False, method=["GET", ])
    def to_draft_d(self, request, *args, **kwargs):
        artist = Artist.objects.get(id=id)
        artist.pb_to_df()
        return Response(data={"message": "data changes to draft"})


class AlbomViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = AlbomSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


    def get_queryset(self):
        return Albom.objects.filter(status='pb')


    @action(detail=True, methods=["GET", ])
    def listen(self, request, *args, **kwargs):
        albom = self.get_object()
        albom.listen += 1
        albom.save()
        return Response(data={"listened": albom.listen})



    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        alboms = self.get_queryset().order_by("-listen")[:3]
        serializer = AlbomSerializerTelegram(alboms, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



    @action(detail=False, method=["GET", ])
    def null_listen(self, request, *args, **kwargs):
        alboms = self.get_queryset().filter(listen=0)
        serializer = AlbomSerializerTelegram(alboms, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)



    @action(detail=False, methods=["GET", ])
    def all_listen(self, request, *args, **kwargs):
        alboms = Albom.objects.all()
        for albom in alboms:
            albom.listen += 1
            albom.save()
        return Response(data={"message": "all albom music listened"})


    @action(detail=False, method=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        alboms = self.get_queryset()  # Songs.objects.all()
        for albom in alboms:
            albom.pb_to_df()
        return Response(data={"message": "all data changes to draft"})


    @action(detail=False, method=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        alboms = Albom.object.all()
        for albom in alboms:
            albom.df_to_pb()
        return Response(data={"message": "all data changes to publish"})


    @action(detail=False, method=["GET", ])
    def to_publish_d(self, request, *args, **kwargs):
        albom = self.get_object()
        albom.df_to_pb()
        return Response(data={"message": "data changes to publish"})

    @action(detail=False, method=["GET", ])
    def to_draft_d(self, request, *args, **kwargs):
        albom = Albom.objects.get(id=id)
        albom.pb_to_df()
        return Response(data={"message": "data changes to draft"})





class SongsViewSetTelegram(viewsets.ModelViewSet):
    serializer_class = SongsSerializerTelegram
    permission_classes = [IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]


    def get_queryset(self):
        return Songs.objects.filter(status='pb')


#Qo'shiqlar eshitilganda listened bittadan qo'shiladi
    @action(detail=True, methods=["GET", ])
    def listen(self, request, *args, **kwargs):
        song = self.get_object()
        song.listen += 1
        song.save()
        return Response(data={"listened": song.listen})


#Eng ko'p eshitilgan 3ta qo'shiqlar ro'yhati
    @action(detail=False, methods=["GET", ])
    def top(self, request, *args, **kwargs):
        #1-variant
        songs = self.get_queryset().order_by("-listen")[:3]
        #2-variant
        # songs = self.get_queryset().order_by("listen")[-3::]
        serializer = SongsSerializerTelegram(songs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


#Biror marta listen bo'lmagan qo'shiqni chiqarish
    @action(detail=False, method=["GET", ])
    def null_listen(self, request, *args, **kwargs):
        songs = self.get_queryset().filter(listen=0)
        serializer = SongsSerializerTelegram(songs, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


#Bracha qo'shiqlarga bittadan listen qo'shish
    @action(detail=False, methods=["GET", ])
    def all_listen(self, request, *args, **kwargs):
        songs = Songs.objects.all()
        for song in songs:
            song.listen += 1
            song.save()
        return Response(data={"message": "all music listened"})


    @action(detail=False, method=["GET", ])
    def to_draft(self, request, *args, **kwargs):
        songs = self.get_queryset()  # Songs.objects.all()
        for song in songs:
            song.pb_to_df()
        return Response(data={"message": "all data changes to draft"})


    @action(detail=False, method=["GET", ])
    def to_publish(self, request, *args, **kwargs):
        songs = Songs.object.all()
        for song in songs:
            song.df_to_pb()
        return Response(data={"message": "all data changes to publish"})


    @action(detail=False, method=["GET", ])
    def to_publish_d(self, request, *args, **kwargs):
        song = self.get_object()
        song.df_to_pb()
        return Response(data={"message": "data changes to publish"})

    @action(detail=False, method=["GET", ])
    def to_draft_d(self, request, *args, **kwargs):
        song = Songs.objects.get(id=id)
        song.pb_to_df()
        return Response(data={"message": "data changes to draft"})



class TokenCheck(APIView):
    def get(self, request):
        from rest_framework.authtoken.models import Token

        token = Token.objects.create(user=request.user)
        print(token.key)
