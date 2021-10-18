from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from teachers.models import Teachers
from courses.models import Course
class TeachersListView(ListView):
    model= Teachers
    template_name= 'teachers.html'
    context_object_name= 'teachers'
    #paginate_by= 1
 #   queryset= Teachers.objects.all()[:1]

class TeacherDetailView(DetailView):
     model = Teachers
     template_name= 'teacher.html'
     context_object_name= 'teacher'


     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True, teacher = self.kwargs['pk'])
        return context