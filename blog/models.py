from django.db import models

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=10)
	phoneNum = models.CharField(max_length=11)
	reason = models.CharField(max_length=100)

	def __str__(self):
		return self.name