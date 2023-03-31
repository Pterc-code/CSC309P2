from django.db import models
from account.models import Account
from reservation.models import Reservation

# Create your models here.

class Notification(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='notification')
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='notification')