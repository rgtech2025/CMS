from django.db import models

# Create your models here.
class Register(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	psw = models.CharField(max_length=10)
	mno = models.CharField(max_length=10)
	addr = models.CharField(max_length=200)