from django.shortcuts import render
from django.views import generic
from equipments.models import ElectronicEquipment, IP
from department.models import Department


class DashboardView(generic.View):

    def get(self, request):
        template_name = 'index.html'
        count_equipments = ElectronicEquipment.objects.all().count()
        count_ip = IP.objects.count()
        count_departments = Department.objects.all().count()
        context = {
            'count_equipments': count_equipments,
            'count_ip': count_ip,
            'count_departments': count_departments,
        }
        return render(request, template_name, context)
