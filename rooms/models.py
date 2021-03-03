
from django.db import models#django package first

from django_countries.fields import CountryField#third party app second

from core import models as core_models # packages I made third
from users import models as user_models


# Create your models here.

class Room(core_models.TimeStampedModel):
    """
    Room Model Definition
    Inherent from TimeStampedModel
    """
    
    name = models.CharField(max_length=140) #이건 required임, so don't do 'null=True'
    description = models.TextField()
    country = CountryField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField() #0~24 hours
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)

    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)