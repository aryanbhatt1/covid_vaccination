from datetime import datetime, date
from django.shortcuts import render
from .models import Bookings, home, VaccinationCentre
from .forms import UserSignUpForm, VacinationCentreForm, CityForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import F
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Group
# Create your views here.

def homeView(request):
    print(datetime.now())
    host_url = request.get_host()
    scheme = request.scheme
    home_data = home.objects.all()
    context = {
        'home_data': home_data,
        'host_url': host_url,
        'scheme': scheme,
    }
    return render(request, 'pages/home.html', context)


def SignUpUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        form = User.objects.create_user(username, email, password1)
        form.is_staff=True 
        form.first_name = first_name
        form.last_name = last_name
        form.email = email
        form.save()
        messages.success(request, 'User has been created successfully.')
    else:
        form = UserSignUpForm()

    return render(request, 'pages/user_signup.html', {'form': form})

def UserLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff == True:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Your Username or Password is incorrect.')
            return redirect('login')

    return render(request, 'pages/user_login.html')

@login_required
def landingPage(request):
    city_form = CityForm(request.POST)
    centre = None
    if city_form.is_valid():
        city_selected = request.POST['city']
        centre = VaccinationCentre.objects.all().filter(city__city=city_selected).filter(allowed_candidates__gte=0)
    context = {
        'centre': centre, 
    }   
    form = VacinationCentreForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    
    context['form']=form
    context['city_form'] = city_form
    return render(request, 'pages/landing_page.html', context)

def bookSlot(request, id):
    centre = VaccinationCentre.objects.get(id=id)
    user_id = request.user
    if int(VaccinationCentre.objects.values_list('allowed_candidates', flat=True).filter(id=id)[0])>0 and len(Bookings.objects.all().filter(user=request.user))==0:
        booking = Bookings(user=user_id, centre=centre, timeDate=datetime.now())
        VaccinationCentre.objects.filter(id=id).update(allowed_candidates=F('allowed_candidates')-1)
        booking.save()
    else:
        return HttpResponse("Already Booked Slot...")
    
    return HttpResponseRedirect(reverse('dashboard'))

today = date.today()

def BookingsView(request):
    bookings = Bookings.objects.all().filter(timeDate__gte=today)
    mybookings = Bookings.objects.all().filter(user=request.user)
    context ={
        'bookings': bookings,
        'mybookings': mybookings,
    }

    return render(request, 'pages/bookings.html', context)

def statusVaccinated(request, id):
    Bookings.objects.filter(id=id).update(status="Vaccinated")
    context = {

    }
    return HttpResponseRedirect(reverse('bookings'))