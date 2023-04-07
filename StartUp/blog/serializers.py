from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError

# Serializers for Posts, Categories, Comments, Tags
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description', 'image', 'author', 'category', 'tag', 'created', 'updated',)
        read_only_fields = ('id',)
        model = Post

class CatSerializer(serializers.ModelSerializer):

    class Meta:
        fields= ('id', 'title', 'slug',)
        read_only_fields = ('id',)
        model = Category

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'post', 'name', 'email', 'text', 'created')
        read_only_fields = ('id', 'created', )
        model = Comment

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', )
        read_only_fields = ('id', )
        model = Tag

# Serializers for Login, Register, Logout, User, Password

class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=128)

    class Meta:
        model = User
        fields = ("username", "password")   

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            raise ValidationError({"error": "User doesn't exists!"})
        return super().validate(attrs)

    def create(self, validated_data):
        username = validated_data.get("username")
        user = User.objects.get(username=username)
        token = Token.objects.create(user=user)
        return token

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password1 = serializers.CharField(min_length=6, max_length=128)
    password2 = serializers.CharField(min_length=6, max_length=128)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def validate(self, attrs):
        password1 = attrs.get("password1")
        password2 = attrs.get("password2")
        if password1 != password2:
            raise ValidationError({"error": "password didn't match!"})
        return super().validate(attrs)

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password1'])
        user.save()
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")
        read_only_fields = ("id", )

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(min_length=6, max_length=128, write_only=True)