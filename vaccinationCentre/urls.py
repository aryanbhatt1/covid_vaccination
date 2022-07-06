from contextlib import nullcontext
from django.urls import path, include

from vaccinationCentre.models import Bookings
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('signUp', views.SignUpUser, name="UserSignUp"),
    path('login', views.UserLogin, name='UserLogin'),
    path('dashboard', views.landingPage, name='dashboard'),
    path('users/', include('django.contrib.auth.urls')),
    path('book/<id>', views.bookSlot, name='book'),
    path('dashboard/bookings', views.BookingsView, name='bookings'),
    path('vaccinated/<id>', views.statusVaccinated, name='vaccinated')
]
