from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('test/', views.test),
    path('test2/', views.test2),
    path('cartview/', views.cartview),
    path('delete/', views.delete),
    path('join/', views.join),
    path('hp/', views.hp),
    path('card/', views.card),
    path('fin/', views.fin),
    path('users/', views.users),
    path('hppost/', views.hpPost),
    path('cardorsamsung/', views.cardorsamsung),
    path('pay/', views.pay),
    path('samsung/', views.samsung),
    path('paycheck/', views.paycheck),
    path('done/', views.done),
    path('donepage/', views.donepage),
    path('carts/', views.carts),
    path('cartlist/', views.cartlist),
    path('cartthing/', views.cartthing),
]