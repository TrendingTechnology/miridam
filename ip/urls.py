from django.urls import path
from ip import views

app_name = 'ip'
urlpatterns = [
    path('', views.IpListView.as_view(), name='list'),
    path('cadastrar/', views.register_ipv4, name='register'),

]
