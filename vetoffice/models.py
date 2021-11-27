from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey


# Create your models here.


class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def has_multiple_pets(self):
        return self.patient_set.count() > 1

    def get_absolute_url(self):
        return "/owner/list"


class Patient(models.Model):
    DOG = "DO"
    CAT = "CA"
    BIRD = "BI"
    REPTILE = "RE"
    OTHER = "OT"

    ANIMAL_TYPE_CHOICES = [
        (DOG, "Dog"),
        (CAT, "Cat"),
        (BIRD, "Bird"),
        (REPTILE, "Reptile"),
        (OTHER, "Other")
    ]

    breed = models.CharField(max_length=200)
    pet_name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    owner = ForeignKey(Owner, on_delete=models.CASCADE)
    animal_type = CharField(
        max_length=2, choices=ANIMAL_TYPE_CHOICES, default=OTHER)

    def get_absolute_url(self):
        return "/patient/list"

    def __str__(self):
        return self.pet_name + ", " + self.animal_type

    class Meta:
        ordering = ["pet_name"]
