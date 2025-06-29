from django.urls import path, include
from django.contrib import admin
from . import views
from .views import register
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('music/', views.music, name='music'),
    path('gallery/', views.gallery, name='gallery'),
    path('shop/', views.shop, name='shop'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('music/audio/',views.audio, name='audio'),
    path('music/video/', views.video, name='video'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_details, name='blog_details'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('events/', views.events_list, name='events_list'),
    path('events/<int:event_id>/', views.event_details, name='event_details'),
    

]    