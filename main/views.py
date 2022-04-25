from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, 'index.html')

def makeHistory(request):

    return render(request, 'history.html')

def histFilter(request):

    return render(request, 'filter.html')