from django.db import models
from django.forms import CharField

# Create your models here.
class Gazeteci(models.Model):
    isim = models.CharField(max_length=120)
    soyisim = models.CharField(max_length=120)
    biyografi = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.isim} {self.soyisim}'
class Makale(models.Model):
    yazar = models.ForeignKey(Gazeteci, on_delete=models.CASCADE, related_name='makaleler')
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
    