from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User)
	company = models.CharField(max_length=150)
	address_1 = models.CharField(max_length=100)
	address_2 = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=2)
	zipcode = models.CharField(max_length=10)
	def __unicode__(self):
		return self.user

		


		
	
		