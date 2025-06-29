# theme/urls.py

from django.urls import path, include
from . import views


urlpatterns = [
      # Include URLs from the theme app
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('music/', views.music, name='music'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
]