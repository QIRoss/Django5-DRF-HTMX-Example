from django.urls import path
from . import views

urlpatterns = [
    path('normal-view/', views.normal_view, name='normal_view'),
    path('api/drf-endpoint/', views.drf_endpoint, name='drf_endpoint'),
]