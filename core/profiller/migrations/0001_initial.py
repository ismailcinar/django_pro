# Generated by Django 4.0.3 on 2022-04-03 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=200)),
                ('sehir', models.CharField(blank=True, max_length=200)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profil', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiller',
            },
        ),
        migrations.CreateModel(
            name='ProfilDurum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('durum_mesaji', models.CharField(max_length=200)),
                ('yaratilma_zamani', models.DateTimeField(auto_now_add=True)),
                ('guncellenme_zamani', models.DateTimeField(auto_now=True)),
                ('user_profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiller.profil')),
            ],
            options={
                'verbose_name_plural': 'ProfilDurum',
            },
        ),
    ]
