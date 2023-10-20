from django.db import models
from django.urls import reverse_lazy


class About(models.Model):
    content = models.CharField(max_length=250, verbose_name='Bashliq')
    slug = models.SlugField(max_length=100,unique=True,null=True)
    text = models.TextField(verbose_name='Etrafli')
    about_img = models.ImageField(upload_to='About_img/%Y/%m/%d/',verbose_name='About_sekil', blank=True,null=True)
    creted_at = models.DateTimeField(auto_now_add=True,verbose_name='Qeyd_tarixi')
    creted_up = models.DateTimeField(auto_now=True,verbose_name='Yenilenme_tarixi')
    public = models.BooleanField(default=True, verbose_name="Derc_edilib")



    def __str__(self):
        return self.content

    def get_absalute_url_about_page(self):
        return reverse_lazy('about_page', kwargs={'about_slug': self.slug})


    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'

