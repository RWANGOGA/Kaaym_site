# theme/urls.py

from django.urls import path, include
from . import views


urlpatterns = [
  # Include URLs from the theme app
  path('', views.home, name='home'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('about/', views.about, name='about'),
  path('blog/', views.blog_list, name='blog_list'),
  path('blog/<slug:slug>/', views.blog_details, name='blog_details'),
  path('contact/', views.contact, name='contact'),
  path('events/', views.events_list, name='events_list'),
  path('events/<int:event_id>/', views.event_details, name='event_details'),
  path('faq/', views.faq, name='faq'),
  path('gallery/', views.gallery, name='gallery'),
  path('music/', views.music, name='music'),
  path('music/audio/',views.audio, name='audio'),
  path('music/video/', views.video, name='video'),
  path('register/', views.register, name='register'),
  path('shop/', views.shop, name='shop'),
  path('team/', views.team, name='team'),
]