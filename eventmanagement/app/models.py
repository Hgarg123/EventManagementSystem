from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager

GENDER = [('Male', 'Male'), ('Female', 'Female')]


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(unique=True,max_length=100)
    email = models.EmailField(unique=True, null=True , blank=True)
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100,blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_admin = models.BooleanField(_('admin'),default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.username


class Event(models.Model):
    event_id = models.IntegerField(unique=True)
    event_name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='event/static/EventImages/')

    def __str__(self):
        return self.event_name

class Venue(models.Model):
    event = models.ForeignKey(Event,on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='event/static/VenueImages/')
    location = models.CharField(max_length=1000)
    rating = models.DecimalField(decimal_places=2,max_digits=4)
    guests = models.IntegerField()
    wifi_available = models.BooleanField(default=False)
    t4seven_available = models.BooleanField(default=False)
    lightning_available = models.BooleanField(default=False)
    catering_available = models.BooleanField(default=False)
    dj_available = models.BooleanField(default=False)
    normal_plate_rate = models.IntegerField(default=0)
    deluxe_plate_rate = models.IntegerField(default=0)
    royal_plate_rate = models.IntegerField(default=0)

class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue,on_delete=models.CASCADE)
    food_type = models.CharField(max_length=500)
    dinner_type = models.CharField(max_length=500)
    guest_count = models.IntegerField(default=100)
    total_cost = models.IntegerField(default=0)
    date = models.CharField(max_length=100)
    status = models.CharField(max_length=500,default="Pending")
    isPending = models.BooleanField(default=True)



