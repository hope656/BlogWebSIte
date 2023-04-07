from django.urls import path, include
from .views import *

urlpatterns = [
    path('', BlogList.as_view(), name="list"),
    path('api/v1/register/', RegisterAPIView.as_view(), name="register"),
    path('api/v1/login/', LoginAPIView.as_view(), name="login"),
    path('api/v1/logout/', LogoutAPIView.as_view(), name="logout"),
    path('api/v1/posts/', PostList.as_view(), name="posts_list"),
    path('api/v1/post/<int:pk>/', PostDetail.as_view(), name="post_detail"),
    path('api/v1/cats/', CatList.as_view(), name="cats_list"),
    path('api/v1/cat/<int:pk>/', CatDetail.as_view(), name="cats_datal"),
    path('api/v1/tags/', TagList.as_view(), name="tags_list"),
    path('api/v1/tag/<int:pk>/', TagDetail.as_view(), name="tags_detal"),
    path('api/v1/comments/', CommentList.as_view(), name='comments_list'),
    path('api/v1/comment/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
    path("cat/<slug:cat_slug>/", CategoryDetail.as_view(), name="cat_detail"),
    path("<slug:slug>/", BlogDeatil.as_view(), name="detail")
]