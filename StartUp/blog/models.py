from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "Category"



class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="post/images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    tag = models.ManyToManyField(Tag, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title 

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
