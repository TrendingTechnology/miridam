from django.urls.base import reverse_lazy
import department
from django.shortcuts import render
from django.views import generic
from department.models import Department


class DepartmentListView(generic.ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'


class DepartmentCreateView(generic.CreateView):
    model = Department
    template_name = 'department_create_update.html'
    fields = '__all__'


class DepartmentDetailView(generic.DetailView):
    model = Department
    context_object_name = 'department'
    template_name = 'department_detail.html'


class DepartmentEditView(generic.UpdateView):
    model = Department
    template_name = 'department_create_update.html'
    fields = '__all__'


class DepartmentDeleteView(generic.DeleteView):
    model = Department
    template_name = 'department_delete.html'
    context_object_name = 'department'
    success_url = reverse_lazy('departments:department_list')
