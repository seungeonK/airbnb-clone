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

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_KOREAN = "korean"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_KRW, "KRW"),
        (CURRENCY_USD, "USD")
    )
    # 이건 기존에 있던 데이터베이스에 새로 추가된
    # column이다. 그니까 bio값이 없을때 그 데이터베이스가 동작 못함
    # 그러니까 default라는 argument를 넣어서 값이 없을 때는 빈칸으로 처리

    # 다른 방법으론 (), 이건 비어있어도 상관없다는 뜻
    avatar = models.ImageField(blank=True, null=True)  # blank는 required가 필요없는거
    gender = models.CharField(
        choices=GENDER_CHOICES, 
        max_length=10,
        blank=True,
    )

    bio = models.TextField(blank=True)
    birthday = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, 
        max_length=256,
        blank=True,
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, 
        max_length=3,
        blank=True,
    )
    superhost = models.BooleanField(default=False)