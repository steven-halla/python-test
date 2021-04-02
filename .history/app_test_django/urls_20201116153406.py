from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register_new_user),
    #this is our mainpage
    path('dashboard', views.view_dashboard),
    path('trips/edit/<int:trip_id>', views.view_trip),
    path('logout', views.logout),
    path('login', views.login),
]
