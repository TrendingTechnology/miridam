from django.urls import path
from ip import views

app_name = 'ip'
urlpatterns = [
    path('', views.list_ipv4, name='list_ipv4'),
    path('cadastrar_ipv4/', views.register_ipv4, name='register_ipv4'),

]
