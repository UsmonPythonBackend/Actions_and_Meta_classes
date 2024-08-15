from django.urls import path, include
from rest_framework import routers
from .views import ArtistViewSetWeb, ArtistViewSetTelegram, AlbomViewSetWeb, AlbomViewSetTelegram, SongsViewSetWeb, SongsViewSetTelegram
from rest_framework.authtoken.views import obtain_auth_token


router = routers.DefaultRouter()
router.register(r'artists-web', ArtistViewSetWeb, basename='artists-web')
router.register(r'artists-telegram', ArtistViewSetTelegram, basename='artists-telegram')
router.register(r'albom-web', AlbomViewSetWeb, basename='albom-web')
router.register(r'albom-telegram', AlbomViewSetTelegram, basename='albom-telegram')
router.register(r'songs-web', SongsViewSetWeb, basename='songs-web')
router.register(r'songs-telegram', SongsViewSetTelegram, basename='songs-telegram')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth-token/', obtain_auth_token),
]