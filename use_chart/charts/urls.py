# charts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chart-data/', views.chart_data, name='chart_data'),
    path('', views.chart_view, name='chart_view'),
]