from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.view_dashboard
]
