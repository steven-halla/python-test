from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.reg)
    path('dashboard', views.view_dashboard),
    path('logout', views.logout),
    path('login', views.login)
]
