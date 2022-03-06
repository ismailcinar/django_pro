from multiprocessing import context
from django.shortcuts import render
from django.views.generic.list import ListView
from teachers.models import Teacher

class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers' # bunu yazdığımız için html içindeki yeri teacher in teachers yazabiliriz
    #queryset = Teacher.objects.all()[:1]
# Create your views here.
    def get_queryset(self):
        return  Teacher.objects.all()[:3] # içeride kaç tane göstermek istediğmizi seçiyoruz
    
    # paginate_by kullanarak da bunu sağlayabiliriz html koduna hazır kod yerleştirerek