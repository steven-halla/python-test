from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    return render(request, "index.html")


def register_new_user(request):
    # creates a new user and redirects them to main page

    errors = User.objects.user_registration_validator(request.POST)

    
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
#logs in user and redirects to main page

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


#ends session and redirects to reg/log in page
def logout(request):
    request.session.clear()
    return redirect("/")


#view the main page here and renders html for dash board
def view_dashboard(request):
    if 'user_id' not in request.session:
        return redirect("/")
    
    user = User.objects.get(id=request.session['user_id'])
    user_trips = Trip.objects.filter(uploaded_by_id=request.session['user_id'])
    context = {
        "user": user,
        "user_trips": user_trips
    }
    print(user_trips)
    return render(request, "dashboard.html", context)

def view_trip(request, trip_id):
    return render(request, "view_trip.html")


def view_edit_trip(request, trip_id):
    errors = Trip.objects.add_trip_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/dashboard/" + str(trip_id) + "/edit")

    trip_to_update = Trip.objects.get(id=trip_id)
    trip_to_update.description = request.POST['title']
    trip_to_update.startdate = request.POST['startdate']
    trip
    trip_to_update.plan = request.POST['desc']
    trip_to_update.save()

    return redirect("/books/" + str(book_id))
    return render(request, "edit_trip.html")


def view_new_trip(request):
    return render(request, "trip_create.html")


def create_trip(request):
    if 'user_id' not in request.session:
        return redirect("/dashboard")

    errors = Trip.objects.add_trip_validator(request.POST)
    print(errors)

    if len(errors) > 0:
        for key, value in errors.items():
            error_msg = key + ' - ' + value
            messages.error(request, error_msg)
        return redirect("/dashboard")

    # current logged in user
    current_user = User.objects.get(id=request.session['user_id'])

    destination_from_post = request.POST['destination']
    startdate_from_post = request.POST['startdate']
    enddate_from_post = request.POST['enddate']
    plan_from_post = request.POST['plan']
    trip = Trip.objects.create(
        destination=destination_from_post,
        plan=plan_from_post,
        startdate=startdate_from_post,
        enddate=enddate_from_post,
        uploaded_by_id=current_user.id,
    )
        
    print(trip)

    #trip.users_who_favorite.add(current_user)

    return redirect("/trips/" + str(trip.id))



