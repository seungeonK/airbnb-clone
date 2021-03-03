from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.RoomType)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass