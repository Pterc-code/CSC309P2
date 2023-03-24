from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# class Address(models.Model):
#     address = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     province = models.CharField(max_length=50)
#     country = models.CharField(max_length=50)
#     postal = models.CharField(max_length=50)

class Property(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    description = models.TextField()
    price = models.FloatField(MinValueValidator(0.0))
    bedroom = models.PositiveIntegerField()
    guest_allowed = models.PositiveIntegerField()
    bathroom = models.PositiveIntegerField()
    bed = models.PositiveIntegerField()

class PropertyPhoto(models.Model):
    image = models.ImageField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE, name="photo")


class Amenity(models.Model):
    name = models.CharField(max_length=50)
    property = models.ManyToManyField(Property, name="amenity")

    
    




