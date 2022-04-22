from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return HttpResponse('Inicio')

def makeHistory(request):

    return HttpResponse('Make History')