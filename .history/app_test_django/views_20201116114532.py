from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def view_index(request):
  
    if 'user_id' in request.session:
        return redirect("/books")

    return render(request, "index.html")
