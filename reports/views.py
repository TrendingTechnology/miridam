from django.shortcuts import render
from django.views import generic


def reports(request):
    template_name = 'reports.html'
    return render(request, template_name)
