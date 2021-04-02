from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def view_index(request):
    #  if user is already logged in, lets not show them login/registration page,
    # and instead redirect them to /books, which is already where we redirect users
    # after they login/register.
    if 'user_id' in request.session:
        return redirect("/books")

    return render(request, "index.html")
