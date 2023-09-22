from django.db import models

class Carusel(models.Model):

    content = models.CharField(max_length=250,verbose_name='Bashliq')
    slug = models.SlugField(max_length=100, unique=True, null=True)
    text = models.TextField(verbose_name='Etrafli')
    carusel_img = models.ImageField(upload_to='Carusel_img/%Y/%m/%d/',verbose_name='Carusel_sekil')
    creted_at = models.DateTimeField(auto_now_add=True,verbose_name='Qeyd_tarixi')
    creted_up = models.DateTimeField(auto_now=True,verbose_name='Yenilenme_tarixi')
    public = models.BooleanField(default=True, verbose_name="Derc_edilib")



    def __str__(self):
        return self.content

    # def get_absalute_url_carusel(self):
    #     return reverse_lazy('carusel', kwargs={'carusel_slug': self.slug})



    class Meta:
        verbose_name = 'Carusel'
        verbose_name_plural = 'Carusel'


class Reklam_b(models.Model):

    content = models.CharField(max_length=250,verbose_name='Bashliq')
    slug = models.SlugField(max_length=100, unique=True, null=True)
    creted_at = models.DateTimeField(auto_now_add=True,verbose_name='Qeyd_tarixi')
    creted_up = models.DateTimeField(auto_now=True,verbose_name='Yenilenme_tarixi')
    public = models.BooleanField(default=True, verbose_name="Derc_edilib")



    def __str__(self):
        return self.content

    # def get_absalute_url_carusel(self):
    #     return reverse_lazy('carusel', kwargs={'carusel_slug': self.slug})



    class Meta:
        verbose_name = 'Reklam'
        verbose_name_plural = 'Reklam'


