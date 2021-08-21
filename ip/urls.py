from django.urls import path
from ip import views

app_name = 'ip'
urlpatterns = [
    path('ip_ativos/', views.IpListView.as_view(), name='active_list'),
    path('ip_inativos/', views.disabled_IP_list, name='disable_list'),
    path('detalhes/<int:pk>/', views.IpDetailView.as_view(), name='detail_ip'),
    path('cadastrar/', views.register_ip, name='register'),
    path('deletar/<int:pk>', views.IpDeleteView.as_view(), name='delete'),
    path('editar/<int:pk>', views.IpUpdateView.as_view(), name='edit'),

    # Department
    path('department/', views.ListDepartment.as_view(), name='department'),
]
