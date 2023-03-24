from django.db import models
from account.models import Account
from property.models import Property

# Create your models here.

class CommentUser(models.Model):
    host = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, related_name='commentuser_host')
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='commentuser_user')
    comment = models.TextField()
    reply = models.PositiveBigIntegerField(default=0)
    
class CommentProperty(models.Model):
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, related_name='commentproperty_user')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='commentproperty_property')
    comment = models.TimeField()
    reply = models.PositiveBigIntegerField(default=0)
