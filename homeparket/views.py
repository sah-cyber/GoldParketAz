from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse_lazy

from carusel.models import Carusel, Reklam_b
from about.models import About
from shop.models import Shop, Contry, Category
from form.models import ContactForm, Contact
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, ListView, DetailView, FormView


class IndexView(TemplateView):
    template_name = 'home_templates/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carusel'] = Carusel.objects.filter(public=True).order_by('-creted_up')
        context['about'] = About.objects.all()
        context['category'] = Category.objects.all()
        context['total_shop'] = Shop.objects.all().count()
        context['reklam'] = Reklam_b.objects.all().order_by('-creted_up')
        return context


# def index(request):
#     carusel = Carusel.objects.all().order_by('-creted_up')
#     about = About.objects.all()
#     category = Category.objects.all()
#     reklam = Reklam_b.objects.all().order_by('-creted_up')
#     context = {
#         'carusel':carusel,
#         'about': about,
#         'category': category,
#         'reklam':reklam,
#
#     }
#     return render(request, 'home_templates/index.html',context)


class AboutView(TemplateView):
    template_name = 'home_templates/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.filter(public=True).order_by('-creted_up')

        return context




def about_page(request, about_slug):
    about_page = About.objects.all().filter(slug=about_slug)
    context = {
        'about_page': about_page,
    }
    return render(request, 'home_templates/about_page.html', context)



class ShopView(ListView):
    model = Shop
    template_name = 'home_templates/shop.html'
    paginate_by = 4
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = Shop.objects.all().filter(public=True).order_by('-creted_up')
        context['category'] = Category.objects.all()
        context['category_total'] = Category.objects.all().count()
        return context


# def shop(request):
#
#     shop = Shop.objects.all().order_by('-creted_up')
#     contry = Contry.objects.all()
#     paginator = Paginator(shop, 4)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     category = Category.objects.all()
#
#     context = {
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




# def contact(request):
#
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         mesaces = SuccessMessageMixin()
#         if form.is_valid():
#             form.save()
#             form = ContactForm()
#             mesaces.success_message
#     else:
#         form = ContactForm()
#
#     context = {
#         'form': form,
#         'mesaces': mesaces,
#
#     }
#
#     return  render(request,'home_templates/contact.html',context)


def shop_page(request):
    shop = Shop.objects.all().order_by('-creted_up')
    context = {
        'shop': shop,
    }
    return render(request, 'home_templates/shop_page.html', context)



def shop_page_one(request, shop_slug):
    shop_p_one = Shop.objects.all().filter(slug=shop_slug)
    context = {
        'shop_p_one': shop_p_one,
    }
    return render(request, 'home_templates/shop_page_one.html', context)



class CategoryDetailView(DetailView):
    # specify the model to use
    model = Category
    template_name = 'home_templates/category_page.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.filter(id=self.kwargs['pk'])
        return context

# def category(request, cat_id):
#     category = Category.objects.filter(pk=cat_id)
#     shop = Shop.objects.all()
#
#     context = {
#         'category': category,
#         'shop' :shop,
#     }
#
#     return render(request, 'home_templates/category_page.html',context)
#

# def email_adres(request):
#     # mesajes = SuccessMessageMixin()
#     # mesaj = mesajes.success_message = 'your recivied your request'
#     contact = ContactForm()
#     context = {
#         'contakt':contact,
#         # 'mesaj': mesaj,
#     }
#
#     return render(request, 'home_templates/send_sms.html', context)
