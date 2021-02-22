from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'author', 'title', 'body', 'total_likes', 'created_at',)
        model = Post


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)


class FanSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'username',
            'full_name',
        )

    @staticmethod
    def get_full_name(obj):
        return obj.get_full_name()