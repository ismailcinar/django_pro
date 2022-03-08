from datetime import timezone
from multiprocessing import context
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from teachers.models import Teacher
from courses.models import Course
class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers.html'
    context_object_name = 'teachers' # bunu yazdığımız için html içindeki yeri teacher in teachers yazabiliriz
    #queryset = Teacher.objects.all()[:1]
# Create your views here.
    def get_queryset(self):
        return  Teacher.objects.all()[:3] # içeride kaç tane göstermek istediğmizi seçiyoruz
    
    # paginate_by kullanarak da bunu sağlayabiliriz html koduna hazır kod yerleştirerek,
class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teacher.html'
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True, teacher = self.kwargs['pk'])
        return context