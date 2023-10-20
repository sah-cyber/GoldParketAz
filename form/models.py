from django.db import models

from django import forms






class Contact(models.Model):
    name = models.CharField(max_length=100,verbose_name="Ad")
    slug = models.SlugField(max_length=100,unique=True,null=True)
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=11, verbose_name="Telefon")
    text = models.TextField(verbose_name='Etrafli')
    creted_at = models.DateTimeField(auto_now_add=True,verbose_name='Qeyd_tarixi')
    creted_up = models.DateTimeField(auto_now=True,verbose_name='Yenilenme_tarixi')
    public = models.BooleanField(default=True, verbose_name="Derc_edilib")




    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    # def get_absalute_url_shop_page_one(self):
    #     return reverse_lazy('shop_page_one', kwargs={'shop_slug': self.slug})



class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name','email','phone','text']
        widgets = {
            'name':forms.TextInput(attrs={'placeholder': 'Adiniz','class' :'mail_text'}),
            'text': forms.Textarea(attrs={'placeholder':'Mesajiniz', 'rows': 5,'class':'massage-bt'}),
            'email': forms.TextInput(attrs={'placeholder':'Email','class' :'mail_text'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon:','class' :'mail_text'})
        }








    # name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Adiniz','class' :'mail_text'}))
    # text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Mesajiniz', 'rows': 5,'class':'massage-bt'}))
    # email = forms.EmailField(required=False,widget=forms.TextInput(attrs={'placeholder':'Email','class' :'mail_text'}))
    # phone = forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'placeholder': 'Tel:','class' :'mail_text'}))











