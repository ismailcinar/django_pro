from django.db import models
from django.forms import CharField

# Create your models here.

class Makale(models.Model):
    yazar = models.CharField(max_length=100)
    baslik = models.CharField(max_length=100)
    aciklama = models.CharField(max_length=250)
    metin = models.TextField()
    sehir = models.CharField(max_length=200)
    yayinlanma_tarihi = models.DateField()
    aktif = models.BooleanField(default=True)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)  # değişmez
    güncellenme_tarihi = models.DateTimeField(auto_now=True)     # değişir


    def __str__(self):
        return self.baslik  # bu methodu adminde görüyoruz
    