from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Shop,Contry,Category



class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','get_shop_img','creted_at', 'creted_up', 'public')
    search_fields = ('name',)
    list_display_links = ('id', 'name')
    list_editable = ('public',)
    list_filter = ('public', 'name')
    prepopulated_fields = {'slug': ('name',)}


    def get_shop_img(self, object):
        return mark_safe(f"<img src = '{object.shop_img.url}' width=30>")

    get_shop_img.short_description = 'Shop_img'


admin.site.register(Shop,ShopAdmin)




class ContryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Contry,ContryAdmin)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Category,CategoryAdmin)
