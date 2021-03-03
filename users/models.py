from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),  # ("male", "Male")
        (GENDER_FEMALE, "Feale"),
        (GENDER_OTHER, "Other"),
    )

    avatar = models.ImageField(null=True, blank=True)  # blank는 required가 필요없는거
    gender = models.CharField(
        choices=GENDER_CHOICES, 
        max_length=10, 
        null=True, 
        blank=True
    )
    # 이건 기존에 있던 데이터베이스에 새로 추가된
    # column이다. 그니까 bio값이 없을때 그 데이터베이스가 동작 못함
    # 그러니까 default라는 argument를 넣어서 값이 없을 때는 빈칸으로 처리

    # 다른 방법으론 (null=True), 이건 비어있어도 상관없다는 뜻
    bio = models.TextField(default="", blank=True)
