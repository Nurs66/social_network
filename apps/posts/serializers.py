from rest_framework import serializers

from apps.posts import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = (
            'id',
            'title',
            'description',
            'owner',
            'created_at',
        )
        read_only_fields = (
            'id',
            'owner',
            'created_at',
        )


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = (
            'id',
            'user',
            'post',
            'date',
        )
        read_only_fields = (
            'id',
            'user',
            'date',
        )
