from django.shortcuts import render
from django.views import generic


class DashboardView(generic.View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
