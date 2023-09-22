from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Carusel,Reklam_b



class CaruselAdmin(admin.ModelAdmin):
    list_display = ('id','content','get_img_carusel','creted_at','creted_up','public')
    search_fields = ('content',)
    list_display_links = ('id','content')
    list_editable = ('public',)
    list_filter = ('public', 'content')
    prepopulated_fields = {'slug': ('content',)}

    def get_img_carusel(self, object):
        return mark_safe(f"<img src = '{object.carusel_img.url}' width=50>")

    get_img_carusel.short_description = 'Carusel_img'


admin.site.register(Carusel,CaruselAdmin)



class Reklam_bAdmin(admin.ModelAdmin):
    list_display = ('id','content','creted_at','creted_up','public')
    search_fields = ('content',)
    list_display_links = ('id','content')
    list_editable = ('public',)
    list_filter = ('public', 'content')
    prepopulated_fields = {'slug': ('content',)}






admin.site.register(Reklam_b,Reklam_bAdmin)
