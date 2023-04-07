from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views import View
from django.db.models import Q
from rest_framework import generics
from .serializers import *
from rest_framework.permissions import * 
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import *

class BlogList(View):
    def get(self, request):
        posts = Post.objects.all()
        search = request.GET.get("search")
        if search:
            posts = Post.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))
        cats = Category.objects.all()
        tags = Tag.objects.all()
        return render(request, "blog/list.html", {"posts": posts, "cats": cats, "tags": tags}) 
    
    def post(self, request):
        pass

class BlogDeatil(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        comments = Comment.objects.filter(post=post)
        return render(request, "blog/detail.html", {"post": post, "comments": comments})

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        Comment.objects.create(name=name, email=email, text=comment, post=post)
        return redirect('detail', slug)

class CategoryDetail(View):
    def get(self, request, cat_slug):
        cats = Category.objects.all()
        category = get_object_or_404(Category, slug=cat_slug)
        # comments = Comment.objects.filter(category=category)
        posts = Post.objects.filter(category=category)
        return render(request, "blog/list.html", {"posts": posts, "cats": cats})

# CRUD -> Posts, Categories, Tags, Comments

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]

class CatList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer
    permission_classes = [IsAdminUser]

class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CatSerializer
    permission_classes = [IsAdminUser]

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAdminUser]

# Register, Logim, Logout

class RegisterAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({})

class LoginAPIView(APIView):
    permission_classes = (AllowAny, )
        

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        return Response({"key": token.key})

class LogoutAPIView(APIView):
    def post(self, request):
        request.user.auth_token.delete()        
        return Response({"detail": "Successfully loged out"})

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAdminUser, )

    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data["password"])
            user.save()
            return Response({"status": "Password Set"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def recent_users(self, request):
        return Response({"detail" "Working..."})