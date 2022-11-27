from django.db import models
from django.utils import timezone

# Create your models here.
class Person(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    height = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    weight = models.IntegerField()
    birthdate = models.DateField(blank=True, default=timezone.now)
    
    def __str__(self):
        return self.lastname

class Position(models.Model):
    description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.description

class Club(models.Model):
    name = models.CharField(max_length=100)
    coach = models.ForeignKey(Person, on_delete=models.CASCADE)
    dorm_latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    dorm_longtitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    team_pic = models.ImageField(default="defaultimg.png", null=True, blank=True, verbose_name="Team Image")
    
    def __str__(self):
        return self.name

class Play(models.Model):
    player = models.ForeignKey(Person, on_delete=models.CASCADE)
    team = models.ForeignKey(Club,on_delete=models.CASCADE)
    string_no = models.IntegerField()
    pos = models.ForeignKey(Position, on_delete=models.CASCADE)
    isActive = models.BooleanField(default=False, verbose_name="Zoning Fee")
    
    def __str__(self):
        return self.player