# Generated by Django 4.0.3 on 2022-03-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.tag'),
        ),
    ]
