from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username','email','password','first_name','last_name',
                  'images_profile','website','bio']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class PostLikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializers(serializers.ModelSerializer):
    users = PostLikeSerializers(read_only=True,many=True)
    class Meta:
        model = UserProfile
        fields = ['users']

class FollowSerializers(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'


class PostSerializers(serializers.ModelSerializer):
    post_like = PostLikeSerializers(read_only=True,many=True)
    class Meta:
        model = Post
        fields = ['post_like']


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentLikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'

class StorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = '__all__'


class  SaveUserSerializers(serializers.ModelSerializer):
    class Meta:
        model =  SaveUser
        fields = '__all__'

class SaveItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = SaveItem
        fields = '__all__'

class PostRatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostRating
        fields = '__all__'

class ChatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

