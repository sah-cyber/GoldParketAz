from django.urls import path
from . views import IndexView,AboutView,CategoryDetailView,ShopView,ContactFormView



from . import views

urlpatterns = [
    path('', IndexView.as_view(),  name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('shop_page/', views.shop_page, name='shop_page'),
    path('shop_page_one/<slug:shop_slug>/', views.shop_page_one, name='shop_page_one'),
    path('about_page/<slug:about_slug>/', views.about_page, name='about_page'),
    #path('email_send/', views.email_adres, name='email_send'),
    #path('contact/', views.email_adres, name='contact'),
    path('category/<int:pk>/',CategoryDetailView.as_view(), name='category'),
    path('shop/', ShopView.as_view(), name = 'shop'),

]