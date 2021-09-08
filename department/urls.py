from django.urls import path
from department import views

app_name = 'departments'
urlpatterns = [
    path('lista/', views.DepartmentListView.as_view(), name='department_list')
]
