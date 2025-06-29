# theme/urls.py

from django.urls import path, include
from . import views
from .views import home

urlpatterns = [
      # Include URLs from the theme app
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),    # This will serve home.html at /
]
