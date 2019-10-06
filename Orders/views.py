from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, "Orders/index.html")

def AddOrder(request):
    return HttpResponse("<h2>orders</h2>")