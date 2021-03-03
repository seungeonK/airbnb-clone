
from django.db import models#django package first

from django_countries.fields import CountryField#third party app second

from core import models as core_models # packages I made third
from users import models as user_models


# Create your models here.


class AbstractItem(core_models.TimeStampedModel):

    name = models.CharField(max_length=80)

    """ Abstract Item """
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class RoomType(AbstractItem):
    """ RoomType Model Definition """
    pass


class Amenity(AbstractItem):
    """ Amenity Model Definition """
    pass


class Facility(AbstractItem):
    """ Facility Model Definition"""
    pass


class HouseRule(AbstractItem):
    """ House Rule Model Definition"""
    pass

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
    
    #많은 룸이 하나의 호스트를 가리킬 수 있음
    #on_delete = 연결돼 있는 model(유저)가 delete되면 어떻게 할거냐?
    #models.CASCADE = 삭제하면, 이 room도 삭제하라.
    #마치 폭포수처럼, 위(user)가 지워지면, 아래(ROOMS)도 지워짐
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    #하나의 룸이 하나의 룸 타입을 가질 수 있고, 하나의 룸타입이 여러개의 룸을 가질 수 있다.
    #만약, 룸타입 하나를 삭제해도, 룸이 삭제되면 안되니까, 
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    #하나의 룸이 여러개의 어메니티 가질 수 있음, 하나의 어메니티를 여러 룸이 동시에 가질 수도 있음
    amenitites = models.ManyToManyField(Amenity)
    facilities = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)





    def __str__(self):
        return self.name