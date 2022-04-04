from django.contrib.auth.models import User
from profiller.models import Profil, ProfilDurum
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profil(sender, instance, created, **kwargs):
    print(instance.username, '__Created', created)
    if created:
        Profil.objects.create(user=instance)
         # her defasında farklı bir nesne için profil oluşturuyoruz

@receiver(post_save, sender=Profil)
def create_durum_mesaji(sender, instance, created, **kwargs):
    if created:
        ProfilDurum.objects.create(user_profil=instance,
        durum_mesaji = f'{instance.user.username} kulübe katıldı'
        
        )
        