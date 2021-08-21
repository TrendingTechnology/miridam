from django.urls import path
from department import views

app_name = 'department'
urlpatterns = [
    path('', views.department, name='teste')
]
