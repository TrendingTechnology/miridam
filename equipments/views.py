from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from equipments.forms import IpForm, ElectronicEquipmentForm
from equipments.models import IP, ElectronicEquipment
from django.views import generic


class IpListView(generic.ListView):
    model = IP
    template_name = 'ip/list_ip.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_all_ip'] = IP.objects.filter(activated=True)
        return context


def disabled_IP_list(request):
    template_name = 'ip/list_ip.html'
    list_all_ip = IP.objects.filter(activated=False)
    context = {'list_all_ip': list_all_ip}
    return render(request, template_name, context)


def register_ip(request):
    if request.method == "POST":
        form = IpForm(request.POST)
        if form.is_valid():
            ip = form.save(commit=False)
            ip.save()
            return redirect('ip:list')
    else:
        form = IpForm()
    return render(request, 'ip/register.html', {'form': form})


class IpDeleteView(generic.DeleteView):
    model = IP
    template_name = 'ip/delete.html'
    success_url = reverse_lazy('equipments:list')


class IpDetailView(generic.DeleteView):
    model = IP
    template_name = 'ip/detail.html'
    context_object_name = 'equipments'


class IpUpdateView(generic.UpdateView):
    model = IP
    template_name = 'ip/update.html'
    fields = '__all__'


class ElectronicEquipmentListView(generic.ListView):
    template_name = 'equipment/equipments_list.html'
    model = ElectronicEquipment
    context_object_name = 'equipments'


class ElectronicEquipmentEditView(generic.UpdateView):
    model = ElectronicEquipment
    fields = '__all__'
    template_name = 'equipment/equipments_edit.html'
    success_url = reverse_lazy('equipments:equipments')


class ElectronicEquipmentCreateView(generic.CreateView):
    form_class = ElectronicEquipmentForm
    template_name = 'equipment/equipments_edit.html'
    success_url = reverse_lazy('equipments:equipments')


class ElectronicEquipmentDeleteView(generic.DeleteView):
    model = ElectronicEquipment
    template_name = 'equipment/equipment_delete.html'
    success_url = reverse_lazy('equipments:equipments')
