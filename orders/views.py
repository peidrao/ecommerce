import json
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from carts.models import CartItem
from store.models import Product

from .models import Order, Payment, OrderProduct
from .forms import OrderForm

def payments(request):
    pass


def place_order(request, total=0, quantity=0):
    pass

def order_complete(request):
    pass
