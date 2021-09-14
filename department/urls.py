from django.urls import path
from department import views

app_name = 'departments'
urlpatterns = [
    path('lista/', views.DepartmentListView.as_view(), name='department_list'),
    path('adicionar/', views.DepartmentCreateView.as_view(),
         name='department_create'),
    path('detalhes/<int:pk>', views.DepartmentEditView.as_view(),
         name='department_edit'),
    path('editar/<int:pk>', views.DepartmentDetailView.as_view(),
         name='department_detail'),
    path('deletar/<int:pk>', views.DepartmentDeleteView.as_view(),
         name='department_delete')
]
