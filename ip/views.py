from django.shortcuts import render, redirect
from ip.forms import Ipv4Form
from ip.models import IPv4


def list_ipv4(request):
    template_name = 'index.html'
    list_all_ipv4 = IPv4.objects.filter(activated=True)
    context = {'list_all_ipv4': list_all_ipv4}
    return render(request, template_name, context)


def register_ipv4(request):
    if request.method == "POST":
        form = Ipv4Form(request.POST)
        if form.is_valid():
            ipv4 = form.save(commit=False)
            ipv4.save()
            return redirect('ip:list_ipv4')
    else:
        form = Ipv4Form()
    return render(request, 'register_ipv4.html', {'form': form})
