from django.shortcuts import render
from django.views import generic
from department.models import Department


class DepartmentListView(generic.ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'


class DepartmentCreateView(generic.CreateView):
    model = Department
    template_name = 'department_create.html'
    fields = '__all__'


class DepartmentDeleteView(generic.DeleteView):
    pass
