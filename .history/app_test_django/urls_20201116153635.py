from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register_new_user),
    path('login', views.login),
    path('logout', views.logout),

    #this is our mainpage
    path('dashboard', views.view_dashboard),

    path('trips/<int:trip_id>', views.view_trip),
    # page to edit trip
    path('trips/edit/<int:trip_id>', views.view_trip),
    # page to create new trip
    path('trip/new', views.view_trip),
    #leads to function to create the trip
    path('trip/create', views.create_trip),

]
