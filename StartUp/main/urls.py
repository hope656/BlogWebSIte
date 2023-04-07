from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    path('services/', services, name="services"),
    path('contact/', contact, name="contact"),
    path('price/', blog_price, name="price"),
    path('feature/', blog_feature, name="feature"),
    path('testimonial/', blog_testimonial, name="testimonial"),
    path('team/', blog_team, name="team"),
    path('quote/', blog_quote, name="quote")
]