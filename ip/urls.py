from django.urls import path
from ip import views

app_name = 'ip'
urlpatterns = [
    path('', views.IpListView.as_view(), name='list'),
    path('ip_desativados/', views.disabled_IP_list, name='disable-list'),
    path('cadastrar/', views.register_ipv4, name='register'),
    path('deletar/<int:pk>', views.IpDeleteView.as_view(), name='delete'),

]
