
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from carusel.models import Carusel, Reklam_b
from about.models import About
from shop.models import Shop, Contry, Category
from form.models import ContactForm, Contact
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView, DetailView, FormView
from GoldParketAz .settings import DEBUG
from shop .filters import OrderFilter


class IndexView(TemplateView):
    template_name = 'home_templates/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carusel'] = Carusel.objects.filter(public=True).order_by('-creted_up')
        context['about'] = About.objects.all()
        context['category'] = Category.objects.all()
        context['total_shop'] = Shop.objects.all().count()
        context['reklam'] = Reklam_b.objects.all().filter(public=True).order_by('-creted_up')
        context['title'] = 'GoldParketaz'
        return context



class AboutView(TemplateView):
    template_name = 'home_templates/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.filter(public=True).order_by('-creted_up')
        context['title'] = 'Haqqimizda'

        return context




def about_page(request, about_slug):
    about_page = About.objects.all().filter(slug=about_slug)
    context = {
        'about_page': about_page,
        'title': 'Haqimizda',
    }
    return render(request, 'home_templates/about_page.html', context)



class ShopView(ListView):
    model = Shop
    template_name = 'home_templates/shop.html'
    context_object_name = 'shop'
    paginate_by = 4


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Mehsulun sayi
        if Shop.public:
            context['category_lak'] = Shop.objects.filter(categoriya__name='Parket laki',public=True).count()
            context['category_kleyi'] = Shop.objects.filter(categoriya__name='Parket kleyi',public=True).count()
            context['diger'] = Shop.objects.filter(categoriya__name='Diger',public=True).count()
            context['parket'] = Shop.objects.filter(categoriya__name='Parket',public=True).count()
            context['title'] = 'Mehsullarimiz'
            return context

    def get_queryset(self):
        return Shop.objects.filter(public=True).order_by('creted_up')


class SearchView(ListView):
    template_name = 'home_templates/search.html'
    model = Shop
    context_object_name = 'shop'
    paginate_by = 4


    def get_queryset(self):
        return Shop.objects.filter(name__icontains=self.request.GET['q'])




    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Netice'
        context['q'] = self.request.GET.get('q')
        return context





# def search(request):
#
#     shop = Shop.objects.all().order_by('-creted_up')
#     contry = Contry.objects.all()
#     paginator = Paginator(shop, 4)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     category = Category.objects.all()
#     if 'q' in request.GET:
#         q = request.GET['q']
#         data = Shop.objects.filter(name__icontains=q)
#     data = Shop.objects.all().filter(public=True).order_by('-creted_up')
#
#
#     context = {
#         'data':data,
#         'shop': page_obj,
#         'contry':contry,
#         'category':category,
#     }
#
#     return render(request, 'home_templates/shop.html',context)


class ContactFormView(SuccessMessageMixin, FormView):
    template_name = 'home_templates/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = "Sizin Mektub Gonderildi"


    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        return context



class CategoryView(ListView):
    template_name = 'home_templates/category_page.html'
    model = Shop
    context_object_name = 'category'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Categoriya'
        return context

    def get_queryset(self):
        return Shop.objects.filter(categoriya__slug=self.kwargs['cats_slug'],public=True)






def shop_page(request):
    shop = Shop.objects.all().filter(public=True).order_by('-creted_at')

    myFilter = OrderFilter(request.GET, queryset= shop)
    shop = myFilter.qs


    context = {
        'shop': shop,
        'title': 'Butun Mehsullar',
        'myFilter': myFilter,
    }
    return render(request, 'home_templates/shop_page.html', context)



def shop_page_one(request, shop_slug):
    shop_p_one = Shop.objects.all().filter(slug=shop_slug).order_by('-creted_up')
    context = {
        'shop_p_one': shop_p_one,
        'title': 'Mehsul',
    }
    return render(request, 'home_templates/shop_page_one.html', context)



class ErorView(TemplateView):
    template_name = 'home_templates/eror.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Sehife Tapilmadi'
        return context
