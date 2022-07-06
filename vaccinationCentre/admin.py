from django.contrib import admin
from .models import home, city, VaccinationCentre, BookAppointment, Bookings
from datetime import datetime
# Register your models here.

@admin.register(home)
class HomeAdmin(admin.ModelAdmin):
    pass

@admin.register(city)
class CityAdmin(admin.ModelAdmin):
    pass

@admin.register(VaccinationCentre)
class VaccinationCentreAdmin(admin.ModelAdmin):
    pass

@admin.register(BookAppointment)
class BookAppointmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Bookings)
class BookingAdmin(admin.ModelAdmin):
    pass
