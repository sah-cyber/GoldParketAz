from django.contrib import admin
from django.utils.safestring import mark_safe
from . models import About

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'content','about_img', 'creted_at', 'creted_up', 'public')
    search_fields = ('content',)
    list_display_links = ('id', 'content')
    list_editable = ('public',)
    list_filter = ('public', 'content')
    prepopulated_fields = {'slug': ('content',)}


    def about_img(self, object):
        return mark_safe(f"<img src = '{object.about_img.url}' width=50>")

    about_img.short_description = 'About_img'


admin.site.register(About, AboutAdmin)

