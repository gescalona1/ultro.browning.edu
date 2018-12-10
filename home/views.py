from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("INDEX")


def about(request):
    return HttpResponse("ABOUT")


def contact(request):
    return HttpResponse("Contact")


def donate(request):
    return HttpResponse("DONATE")
