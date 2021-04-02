from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register_new_user),
    #this is our mainpage
    path('dashboard/<int:trip_id>', views.view_dashboard),
    path('logout', views.logout),
    path('login', views.login),
    #puts us on the path to view add page
    path('trip/add', views.view_trip),
    #leads to function to create the trip
    path('trip/create', views.create_trip)
]
