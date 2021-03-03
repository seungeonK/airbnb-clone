from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


# I want to see 'user' in the admin panel, and the class
# I'm going to control in the admin panel is this->CustomUserAdmin
# = admin.site.register(models.User, CustomUserAdmin)
@admin.register(models.User)# decorate, it takes the following line
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """
    # list_display = ('username', 'email', 'gender', 'language', 'currency', 'superhost')
    # list_filter = ('language', 'currency', 'superhost')
    fieldsets = UserAdmin.fieldsets + (
        (
            "Banana",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthday",
                    "language",
                    "currency",
                    "superhost",
                )
            }
        ),
    )