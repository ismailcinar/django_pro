from django.contrib import admin
from . models import Teacher
# Register your models here.
 
#admin.site.register(Course)
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

