from django.contrib import admin
from .models import AudioTrack, VideoTrack
from.models import Product
from .models import GalleryImage
from.models import BlogPost
from django.utils.text import slugify
from.models import ContactMessage
from.models import TeamMember
from.models import Event

admin.site.register(AudioTrack)
admin.site.register(VideoTrack)
admin.site.register(Product)
admin.site.register(GalleryImage)
admin.site.register(ContactMessage)
admin.site.register(TeamMember)
admin.site.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location' ,'is_past')
    list_filter = ('start_time',)
    search_fields = ('title', 'description')
admin.site.register(BlogPost)

class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
# Register your models here.
