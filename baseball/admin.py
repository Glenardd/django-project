from django.contrib import admin
from django.contrib.admin import display
from .models import Position, Person, Club, Play

# Register your models here.
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):  
    list_display = ("description",)
    search_fields = ("description",)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("lastname","firstname","height","weight","birthdate")
    search_fields = ("lastname","firstname","height","weight","birthdate")

@admin.register(Club)
class Clubadmin(admin.ModelAdmin):
    list_display = ("name", "coach", "dorm_latitude", "dorm_longtitude")
    search_fields = ("name", "coach", "dorm_latitude", "dorm_longtitude")

@admin.register(Play)
class Playadmin(admin.ModelAdmin):
    list_display = ("player", "team", "string_no", "pos", "isActive")
    search_fields = ("player", "team", "string_no", "pos", "isActive")