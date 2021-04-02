from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register_new_user),
    path('login', views.login),
    path('logout', views.logout),

    #this is our mainpage
    path('dashboard', views.view_dashboard),

    # page to view trip details
    path('trips/<int:trip_id>', views.view_trip),
    # TODO add function to handle actual updating of trip

    # page to edit trip
    path('trips/edit/<int:trip_id>', views.view_edit_trip),
    # page to create new trip
    path('trip/new', views.view_new_trip),
    #leads to function to create the trip
    path('trip/create', views.create_trip),

]
