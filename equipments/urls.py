from django.urls import path
from equipments import views

app_name = 'ip'
urlpatterns = [
    path('ip_ativos/', views.IpListView.as_view(), name='active_list'),
    path('ip_inativos/', views.disabled_IP_list, name='disable_list'),
    path('detalhes/<int:pk>/', views.IpDetailView.as_view(), name='detail_ip'),
    path('cadastrar/', views.register_ip, name='register'),
    path('deletar/<int:pk>', views.IpDeleteView.as_view(), name='delete'),
    path('editar/<int:pk>', views.IpUpdateView.as_view(), name='edit'),

    # Department
    path('equipamentos/', views.ElectronicEquipmentListView.as_view(), name='equipments'),
    path('equipamentos/cadastrar/', views.ElectronicEquipmentCreateView.as_view(), name='equipments_create'),
    path('equipamentos/<int:pk>', views.ElectronicEquipmentEditView.as_view(), name='equipments_edit'),
    path('equipamentos/deletar/<int:pk>', views.ElectronicEquipmentDeleteView.as_view(), name='equipments_delete'),
    path('equipamentos/detalhes/<int:pk>', views.ElectronicEquipmentDetailView.as_view(), name='equipments_detail'),
]
