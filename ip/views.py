from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from ip.forms import IpForm
from ip.models import IP, ElectronicEquipment
from django.views import generic


class IpListView(generic.ListView):
    model = IP
    template_name = 'ip/index.html'

    # Definindo um contexto
    def get_context_data(self, *, object_list=None, **kwargs):
        # context recebe um dicionário
        context = super().get_context_data(**kwargs)
        # context 'list_all_ip' recebe uma lista de IP's filtrados pelo status de activated
        context['list_all_ip'] = IP.objects.filter(activated=True)
        # Retorna o context
        return context


def disabled_IP_list(request):
    template_name = 'ip/index.html'
    list_all_ip = IP.objects.filter(activated=False)
    context = {'list_all_ip': list_all_ip}
    return render(request, template_name, context)


def register_ip(request):
    # Se request do usuário for igual a POST
    if request.method == "POST":
        # A variavel form vai receber os dados do request.POST
        form = IpForm(request.POST)
        # Se os dados recebeido pelo form for valido
        if form.is_valid():
            # A Variavel ip vai receber e salvar o form mas não fará o commit para o banco de dados
            ip = form.save(commit=False)
            # Salvando ip (form) no banco de dados
            ip.save()
            # Redireciona para a pagina inicial
            return redirect('ip:list')
    else:
        # Caso o metodo não seja um POST válido ele vai retornar um form vazio
        form = IpForm()
    return render(request, 'ip/register.html', {'form': form})


class IpDeleteView(generic.DeleteView):
    model = IP
    template_name = 'ip/delete.html'
    success_url = reverse_lazy('ip:list')


class IpDetailView(generic.DeleteView):
    model = IP
    template_name = 'ip/detail.html'
    context_object_name = 'ip'


class IpUpdateView(generic.UpdateView):
    model = IP
    template_name = 'ip/update.html'
    fields = '__all__'


class ListDepartment(generic.ListView):
    template_name = 'department/department.html'
    model = ElectronicEquipment
    context_object_name = 'departments'
