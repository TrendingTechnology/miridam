from django.shortcuts import render, redirect
from ip.forms import Ipv4Form
from ip.models import IP
from django.views import generic


class IpListView(generic.ListView):
    model = IP
    template_name = 'index.html'

    # Definindo um contexto
    def get_context_data(self, *, object_list=None, **kwargs):
        # context recebe um dicionário
        context = super().get_context_data(**kwargs)
        # context 'list_all_ip' recebe uma lista de IP's filtrados pelo statuc de activated
        context['list_all_ip'] = IP.objects.filter(activated=True)
        # Retorna o context
        return context


def register_ipv4(request):
    # Se request do usuário for igual a POST
    if request.method == "POST":
        # A variavel form vai receber os dados do request.POST
        form = Ipv4Form(request.POST)
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
        form = Ipv4Form()
    return render(request, 'register.html', {'form': form})
