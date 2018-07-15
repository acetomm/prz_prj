from django.db import models
from django.contrib.auth.models import User

class Deposit(models.Model):
	user_id = models.OneToOneField(User, on_delete=models.CASCADE)
	depo_value = models.IntegerField()

class Auction(models.Model):
	name = models.CharField(max_length=100)
	active = models.BooleanField()
	min_depo = models.IntegerField()
	stages = models.IntegerField()

class Enrolling(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)

class Betting(models.Model):
	enroll_id = models.ForeignKey(Enrolling, on_delete=models.CASCADE)
	timestamp = models.DateTimeField()

class Running(models.Model):
	auction_id = models.ForeignKey(Auction, on_delete=models.CASCADE)
	current_stage = models.IntegerField()
	timestamp = models.DateTimeField()
	
	

