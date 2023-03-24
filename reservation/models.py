from django.db import models
from property.models import Property
from account.models import Account
from django.core.validators import MaxValueValidator

# Create your models here.
class Reservation(models.Model):
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True, related_name='reservation')
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, related_name='reservation')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.PositiveIntegerField(validators=[MaxValueValidator(7)])