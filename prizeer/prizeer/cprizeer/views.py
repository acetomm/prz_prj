from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse

from .models import Deposit, Auction, Enrolling, Betting, Running

def index(request):
	c = {}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		print(username, password, user)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect(reverse('room'))
			else:
				return HttpResponse(
					template.render(
						{'message': 'User isn\'t active'},
						request
					)
				)
		else:
			c['message'] = 'Wrong login or password'
	template = loader.get_template('cprizeer/index.html')
	return HttpResponse(template.render(c, request))

def room(request):
	c = {
		'user_name': request.user.username,
		'user_deposit': request.user.deposit.depo_value,
		'my_enrollings': request.user.enrolling_set.all()
	}
	print(request.user.enrolling_set, dir(request.user.enrolling_set))
	template = loader.get_template('cprizeer/room.html')
	return HttpResponse(template.render(c, request))
	

def auctions(request):
	c = {
		'auctions': Auction.objects.all()
	}
	template = loader.get_template('cprizeer/auctions.html')
	return HttpResponse(template.render(c, request))

def enroll(request, auction_id):
	Enrolling.objects.create(
		user_id=request.user,
		auction_id=Auction.objects.get(pk=auction_id)
	).save()
	return redirect(reverse('room'))

def auction(request, auction_id):
	auction = Auction.objects.get(pk=auction_id)
	c = {
		'enrollings': auction.enrolling_set.all()
	}
	template = loader.get_template('cprizeer/auction.html')
	return HttpResponse(template.render(c, request))

def bet(request, auction_id):
	auction = Auction.objects.get(pk=auction_id)
	enrolling = Enrolling.objects.get(user_id=request.user, auction_id=auction)
	Betting.objects.create(
		enroll_id=enrolling,
		timestamp=datetime.now()
	).save()
	return redirect(reverse('auction', kwargs={'auction_id': auction_id}))


