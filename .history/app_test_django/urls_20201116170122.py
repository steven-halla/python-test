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

    # page to edit trip
    path('trips/edit/<int:trip_id>', views.view_edit_trip),
    # add function to handle actual updating of trip
    path('trips/update/<int:trip_id>', views.edit_trip),
    path('trips/delete/<int:trip_id'>, views.delete_trip)
    # page to create new trip
    path('trips/new', views.view_new_trip),
    #leads to function to create the trip
    path('trips/create', views.create_trip),

]
