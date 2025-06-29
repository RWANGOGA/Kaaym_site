from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.core.paginator import Paginator
from .forms import RegistrationForm
from.models import AudioTrack, VideoTrack
from .models import GalleryImage
from  django.core.paginator import Paginator
from.models import BlogPost
from  django.shortcuts import get_object_or_404
from .models import ContactMessage
from .forms import ContactForm
from.models import TeamMember
from .models import Event
from django.utils import timezone  



def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')
def contact(request):
    return render(request, 'core/contact.html')
def music(request):
    return render(request, 'core/music.html')
def gallery(request):
    return render(request, 'core/gallery.html')
def shop(request):
    return render(request, 'core/shop.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to home or any other page
    else:
        form = RegistrationForm()
    return render(request, 'core/register.html', {'form': form})
def audio(request):
    audio_tracks = AudioTrack.objects.order_by('-created_at')  # Order by creation date, newest first
    return render(request, 'core/audio.html', {'audio_tracks': audio_tracks})

def video(request):
    video_tracks = VideoTrack.objects.order_by('-created_at')  # Order by creation date, newest first
    return render(request, 'core/video.html', {'video_tracks': video_tracks})

def blog_list(request):
    posts =BlogPost.objects.filter(is_published=True).order_by('-created_at') 
    return render (request, 'core/blog_list.html',{'post':posts})

def blog_details(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, 'core/blog_detail.html', {'post': post})  # Order by creation date, newest first

# Create your views here.
def gallery(request):
    images = GalleryImage.objects.order_by('-created_at')  # Order by creation date, newest first
    
    category = request.GET.get('category')
    if category:
        images = images.filter(category=category) 
    paginator =Paginator(images ,12)
    page_number =request.GET.get('page')
    page_obj =paginator.get_page(page_number)
    
         # Filter by category if provided
    return render(request, 'core/gallery.html', {
        'page_obj': page_obj,
        'category': category,  # Pass the selected category to the template
        'categories': GalleryImage.CATEGORY_CHOICES,  
        })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to a success page or home after saving
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form, 'categories': GalleryImage.CATEGORY_CHOICES})
def team(request):
    team_members = TeamMember.objects.order_by('created_at')  # Fetch all team members
    return render(request, 'core/team.html', {'team_members': team_members, 'categories': GalleryImage.CATEGORY_CHOICES})
# Pass categories for filtering})

def events_list(request):
    now = timezone.now()
    upcoming_events = Event.objects.filter(date__gte=now).order_by('date')
    past_events = Event.objects.filter(date__lt=now).order_by('-date')
    return render(request, 'core/events_list.html', {
        'upcoming_events': upcoming_events,'past_events': past_events, 'categories': GalleryImage.CATEGORY_CHOICES})
def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'core/event_details.html', {'event': event, 'categories': GalleryImage.CATEGORY_CHOICES})
