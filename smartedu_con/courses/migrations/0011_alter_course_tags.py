# Generated by Django 4.0.3 on 2022-03-05 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_alter_course_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.tag'),
        ),
    ]
