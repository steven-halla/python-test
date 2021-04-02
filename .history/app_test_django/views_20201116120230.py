from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    return render(request, "index.html")


def register_new_user(request):
    # returns a dictionary of errors.
    # e.g. errors['first_name'] = 'letters only'
    errors = User.objects.user_registration_validator(request.POST)

    # iterate over each error (key/value) pair in the errors dictionary
    # and take the error key and value and makes a full error message,
    # and then adds the error message via messages.error()
    if len(errors) > 0:
        for key, value in errors.items():
            error_msg = key + ' - ' + value
            messages.error(request, error_msg)

        return redirect("/")

    else:
        first_name_from_post = request.POST['first_name']
        last_name_from_post = request.POST['last_name']
        email_from_post = request.POST['email']
        password_from_post = request.POST['password']
        new_user = User.objects.create(
            first_name=first_name_from_post,
            last_name=last_name_from_post,
            email=email_from_post,
            password=password_from_post
        )
        print(new_user.id)
        request.session['user_id'] = new_user.id

        return redirect('/dashboard')


def login(request):
    # user did provide email/password, now lets check database
    email_from_post = request.POST['email']
    password_from_post = request.POST['password']

    # this will return all users that have the email_from_post
    # in future we should require email to be unique
    users = User.objects.filter(email=email_from_post)
    if len(users) == 0:
        messages.error(request, "email/password does not exist")
        return redirect("/")

    user = users[0]
    print(user)

    if (user.password != password_from_post):
        messages.error(request, "email/password does not exist")
        return redirect("/")

    
    request.session['user_id'] = user.id

    return redirect("/dashboard")

def view_dashboard(request):
    return render(request, "dash_board")
