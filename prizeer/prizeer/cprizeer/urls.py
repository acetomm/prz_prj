from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('room/', views.room, name='room'),
	path('auctions/', views.auctions, name='auctions'),
	path('enroll/<int:auction_id>/', views.enroll, name='enroll'),
	path('auction/<int:auction_id>/', views.auction, name='auction'),
	path('bet/<int:auction_id>/', views.bet, name='bet'),
]

