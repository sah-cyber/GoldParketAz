from django.db import models
from django.urls import reverse_lazy


class Contry(models.Model):
    name = models.CharField(max_length=100,verbose_name="Contry")
    slug = models.SlugField(max_length=100,unique=True,null=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Olke'
        verbose_name_plural = 'Olke'



class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="Categoriya")
    slug = models.SlugField(max_length=100,unique=True,null=True)

    def __str__(self):
        return self.name


    def get_absalute_url_category(self):
        return reverse_lazy('category', kwargs={'cats_slug': self.slug})


    class Meta:
        verbose_name = 'Categoriya'
        verbose_name_plural = 'Categoriya'


class Shop(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ad")
    slug = models.SlugField(max_length=100,unique=True,null=True)
    categoriya = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Categoriya')
    contry = models.ForeignKey(Contry,blank=True,null=True, on_delete=models.CASCADE,verbose_name='Olke')
    text = models.TextField(verbose_name='Etrafli',blank=True)
    shop_img = models.ImageField(upload_to='Shop_img/%Y/%m/%d/',verbose_name='Shop_img', blank=True,null=True)
    price = models.DecimalField(default=0, max_digits = 5,decimal_places = 2, verbose_name='Price')
    creted_at = models.DateTimeField(auto_now_add=True,verbose_name='Qeyd_tarixi')
    creted_up = models.DateTimeField(auto_now=True,verbose_name='Yenilenme_tarixi')
    public = models.BooleanField(default=True, verbose_name="Derc_edilib")



    def __str__(self):
        return self.name

    def get_absalute_url_shop_page_one(self):
        return reverse_lazy('shop_page_one', kwargs={'shop_slug': self.slug})


    class Meta:
        verbose_name = 'Mehsullar'
        verbose_name_plural = 'Mehsullar'




