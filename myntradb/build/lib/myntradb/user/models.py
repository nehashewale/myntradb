from django.db import models

class Address(models.Model):
    landmark = models.CharField(max_length=100)
    village = models.CharField(max_length=20)
    taluka = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField(default=True)
 

# Create your models here.
class User(models.Model):
   first_name = models.CharField(max_length=20)
   middle_name = models.CharField(max_length=20)
   last_name = models.CharField(max_length=20)
   phone_number = models.IntegerField(default=True)
   GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
   gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
   primary_address = models.ForeignKey(Address,on_delete=models.CASCADE,related_name = 'primary_address')
   shipping_address = models.ForeignKey(Address,on_delete=models.CASCADE,related_name='shipping_address')
 