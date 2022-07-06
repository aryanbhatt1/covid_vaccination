from datetime import datetime
from statistics import mode
from django.contrib.auth.models import User
from django.db import models
# Create your models here.


class home(models.Model):
    homepage_banner = models.ImageField(upload_to="home_img/", null=True)
    navbar_title = models.CharField("Title", max_length=30, null=True)
    heading = models.CharField('Heading', max_length=30, null=True)
    subheading = models.TextField('Sub Heading', null=True)

    def __str__(self):
        return "Home - {}".format(self.id)

class city(models.Model):
    city = models.CharField('City', max_length=70, null=True)

    def __str__(self):
        return self.city

class VaccinationCentre(models.Model):
    centre_name = models.CharField('Centre Name', max_length=60, null=True)
    address = models.TextField('Address', null=True)
    city = models.ForeignKey(city, on_delete=models.CASCADE, null=True)
    pincode = models.IntegerField('Pin code', null=True)
    allowed_candidates = models.IntegerField('Allowed Candidates', default=10, null=True)

    def __str__(self):
        return self.centre_name

class BookAppointment(models.Model):
    VaccinationCentre = models.ForeignKey(VaccinationCentre, on_delete=models.CASCADE, blank=True, null=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{} - {}".format(self.VaccinationCentre, self.User)

class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    status = models.CharField('Status', max_length=40, default="Not Vaccinated", null=True)
    centre = models.ForeignKey(VaccinationCentre, on_delete=models.CASCADE, null=True)
    timeDate = models.DateTimeField(editable=True,default=datetime.now(), null=True)
    def __str__(self):
        return str(self.timeDate)
