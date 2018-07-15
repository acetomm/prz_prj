from django.contrib import admin
from .models import Deposit, Auction, Enrolling, Betting, Running

admin.site.register(Deposit)
admin.site.register(Auction)
admin.site.register(Enrolling)
admin.site.register(Betting)
admin.site.register(Running)

