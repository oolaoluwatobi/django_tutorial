# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('Hello, World!, ola is here')
    print(request, 'request')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("About me, i'm cool, calm and collected 😎")
    return render(request, 'about.html')