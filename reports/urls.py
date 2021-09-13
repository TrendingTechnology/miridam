from django.urls import path
from reports import views

app_name = 'reports'
urlpatterns = [
    path('', views.ReportsListView.as_view(), name='report_list'),
]
