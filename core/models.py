from django.db import models

class AudioTrack(models.Model):
    title =models.CharField(max_length=200)
    artist =models.CharField(max_length=200,default='KAAYM')
    descritpion = models.TextField(blank=True)
    audio_file = models.FileField(upload_to='audio/', blank=True, null=True )
    external_link = models.URLField(blank=True, help_text='optional:Spotify, YouTube, etc.  ')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class VideoTrack(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200, default='KAAYM')
    description = models.TextField(blank=True)
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    external_link = models.URLField(blank=True, help_text='optional:YouTube, Vimeo, etc.')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title  

class Product(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('CD', 'CD'),
        ('MERCH', 'Merchandise'),
        ('DIGITAL', 'Digital Download'),
        ('SHIRTS', 'Shirts'),
        ('HYMNBOOKS', 'Hymn Books'),
        ('NOTEBOOKS', 'Notebooks'),
        ('UMBRELLAS', 'Umbrellas'),
    ]   
    name = models.CharField(max_length=200) 
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    product_type = models.CharField(max_length=20, choices=PRODUCT_TYPE_CHOICES, default='CD')
    digital_file = models.FileField(upload_to='digital_products/', blank=True, null=True, help_text='For digital downloads only')  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    

class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('worship', 'Worship'),
        ('events', 'Events'),
        ('mission', 'Mission'),
        ('gatetogether', 'Gate to Gather'),
        ('fellowship', 'Fellowship'),
        ('lunch_hour', 'Lunch Hour'),
        ('behind_the_scenes', 'Behind the Scenes'),
    ]

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='worship')

    def __str__(self):
        return self.title  


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True )
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title 

class ContactMessage(models.Model): 
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"   



class TeamMember(models.Model):
    name = models.CharField(max_length=100) 
    position = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='team/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    twitter_link = models.URLField(blank=True, null=True)
    whatsapp =models.CharField(max_length=15, blank=True,  help_text='WhatsApp number in international format (e.g., +1234567890)')
    phone = models.CharField(max_length=15, blank=True, help_text='Phone number in international format (e.g., +1234567890)')
    email = models.EmailField(blank=True, )
    facebook = models.URLField(blank=True, )
    linkedin = models.URLField(blank=True, )

    def __str__(self):
        return self.name
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['start_time']
        verbose_name ='Event'
        verbose_name_plural ='Events'

    def __str__(self):
        return self.title 

    @property
    def is_past(self):
        from django.utils import timezone
        return self.start_time < timezone.now()   


# Create your models here.
