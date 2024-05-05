# from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # return HttpsResponse('This is Home page.')
    return render(request, 'home.html')

def about(request):
    # return HttpsResponse('This is About page.')
    return render(request, 'about.html')