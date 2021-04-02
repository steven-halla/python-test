from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register_new_user),
    path('dashboard', views.view_dashboard),
    path('logout', views.logout),
    path('login', views.login)
   # path('trip/add', views.create_trip)
]
