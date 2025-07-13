from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.core.paginator import Paginator
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.utils import timezone  
from core.forms import RegistrationForm, ContactForm
from core.models import AudioTrack, VideoTrack, GalleryImage, BlogPost, ContactMessage, TeamMember, Event

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
# def contact(request):
#     return render(request, 'contact.html')
def music(request):
    return render(request, 'music.html')

def faq(request):
    return render(request, 'faq.html' )

def gallery(request):
    return render(request, 'gallery.html')
    
def shop(request):
    return render(request, 'shop.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to home or any other page
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})
def audio(request):
    audio_tracks = AudioTrack.objects.order_by('-created_at')  # Order by creation date, newest first
    return render(request, 'audio.html', {'audio_tracks': audio_tracks})

def video(request):
    video_tracks = VideoTrack.objects.order_by('-created_at')  # Order by creation date, newest first
    return render(request, 'video.html', {'video_tracks': video_tracks})

def blog_list(request):
    posts =BlogPost.objects.filter(is_published=True).order_by('-created_at') 
    return render (request, 'blog_list.html',{'post':posts})

def blog_details(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, 'blog_detail.html', {'post': post})  # Order by creation date, newest first

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
    return render(request, 'gallery.html', {
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

    countries = {
        'UG': 'Uganda',
        'KE': 'Kenya',
        'US': 'United States'
    }

    return render(request, 'contact.html', {'form': form, 'categories': GalleryImage.CATEGORY_CHOICES, 'countries': countries })

def team(request):
    team_members = TeamMember.objects.order_by('created_at')  # Fetch all team members
    return render(request, 'team.html', {'team_members': team_members, 'categories': GalleryImage.CATEGORY_CHOICES})
# Pass categories for filtering})

def events_list(request):
    now = timezone.now()
    upcoming_events = Event.objects.filter(date__gte=now).order_by('date')
    past_events = Event.objects.filter(date__lt=now).order_by('-date')
    return render(request, 'events_list.html', {
        'upcoming_events': upcoming_events,'past_events': past_events, 'categories': GalleryImage.CATEGORY_CHOICES})
def event_details(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'event_details.html', {'event': event, 'categories': GalleryImage.CATEGORY_CHOICES})
