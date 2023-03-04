from rest_framework import serializers
from .models import Singer, Song


class SingerSerializer(serializers.ModelSerializer):
    "it will give only id"
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    "song is used from reelated name in models.py file"
    song = serializers.StringRelatedField(many=True, read_only=True)
    "it will give only herf link of song"
    # song = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name='song-detail')
    "it will send any deatil you want example=title,duration,etc."
    # song = serializers.SlugRelatedField(
    #     many=True, read_only=True, slug_field='title')
    "it will give only one song link"
    # song = serializers.HyperlinkedIdentityField(view_name='song-detail')

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']
