from django.db import models
from django.dispatch import receiver
from django.urls import reverse
from django.core.mail import send_mail




# Create your models here.

# this model Stores the data of the Phones Verified
class phoneModel(models.Model):
    Mobile = models.CharField(max_length=20)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)  # For HOTP Verification


    def __str__(self):
        return str(self.Mobile)

