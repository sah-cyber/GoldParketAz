# Generated by Django 4.2.5 on 2023-09-20 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ad')),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=11, verbose_name='Telefon')),
                ('text', models.TextField(verbose_name='Etrafli')),
                ('creted_at', models.DateTimeField(auto_now_add=True, verbose_name='Qeyd_tarixi')),
                ('creted_up', models.DateTimeField(auto_now=True, verbose_name='Yenilenme_tarixi')),
                ('public', models.BooleanField(default=True, verbose_name='Derc_edilib')),
            ],
        ),
    ]
