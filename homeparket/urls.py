from django.urls import path
from . views import IndexView,AboutView,ContactFormView,SearchView,ShopView,CategoryView

from . import views

urlpatterns = [
    path('', IndexView.as_view(),  name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('shop/', ShopView.as_view(), name = 'shop'),
    path('search/', SearchView.as_view(), name = 'search'),
    #
    path('shop_page/', views.shop_page, name='shop_page'),
    path('shop_page_one/<slug:shop_slug>/', views.shop_page_one, name='shop_page_one'),
    path('about_page/<slug:about_slug>/', views.about_page, name='about_page'),
    path('category/<slug:cats_slug>/', CategoryView.as_view(), name='category'),

 ]