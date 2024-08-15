from django.db import models
from .helpers import SaveMediaFiles


class StatusChoice(models.TextChoices):
    DRAFT = 'df', 'Draft',
    PUBLISH = 'pb', 'Publish'

class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=SaveMediaFiles.save_artist_image)
    nick_name = models.CharField(max_length=50)
    listen = models.PositiveBigIntegerField(default=0)
    status = models.CharField(max_length=5, choise=StatusChoice.choices, default=StatusChoice.PUBLISH)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id', ]

    def __str__(self):
        return self.nick_name


    class Meta:
        ordering = ['id', ]
        indexes = [
            models.index(fields=['id']),
        ]


    def df_to_pb(self):
        if self.status == 'df':
            self.status == 'pb'
            self.save()


    def pb_to_df(self):
        if self.status == 'pb':
            self.status == 'df'
            self.save()




class Albom(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to=SaveMediaFiles.save_albom_image)
    description = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    listen = models.PositiveBigIntegerField(default=0)
    status = models.CharField(max_length=5, choise=StatusChoice.choices, default=StatusChoice.PUBLISH)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['id', ]
        indexes = [
            models.index(fields=['id']),
        ]


    def df_to_pb(self):
        if self.status == 'df':
            self.status == 'pb'
            self.save()


    def pb_to_df(self):
        if self.status == 'pb':
            self.status == 'df'
            self.save()




class Songs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to=SaveMediaFiles.save_songs_image)
    listen = models.PositiveBigIntegerField(default=0)
    status = models.CharField(max_length=5, choise=StatusChoice.choices, default=StatusChoice.PUBLISH)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)


    class Meta:
        ordering = ['id', ]
        indexes = [
            models.index(fields=['id']),
        ]


    def df_to_pb(self):
        if self.status == 'df':
            self.status == 'pb'
            self.save()


    def pb_to_df(self):
        if self.status == 'pb':
            self.status == 'df'
            self.save()


    def __str__(self):
        return self.title



class SongsAlbom(models.Model):
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Songs)