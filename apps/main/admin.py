from django.contrib import admin
from apps.main.models import Main, Over, Awards, About, Contact
# Register your models here.

admin.site.register(Main)
admin.site.register(Over)
from django.utils.html import format_html

@admin.register(Awards)
class AwardsAdmain(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="50px" />'.format(obj.image.url))
    list_display = ("image_tag", )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    def video_tag(self, obj):
        return format_html('<video src="{}" width="auto" height="50px" />'.format(obj.video.url))
    
    list_display = ('title', 'description', 'video_tag')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')