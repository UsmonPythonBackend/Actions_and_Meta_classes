# Generated by Django 5.1 on 2024-08-10 21:15

import api.helpers
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=api.helpers.SaveMediaFiles.save_artist_image)),
                ('nick_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Albom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=api.helpers.SaveMediaFiles.save_albom_image)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.artist')),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=api.helpers.SaveMediaFiles.save_songs_image)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.artist')),
            ],
        ),
        migrations.CreateModel(
            name='SongsAlbom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.albom')),
                ('songs', models.ManyToManyField(to='api.songs')),
            ],
        ),
    ]
