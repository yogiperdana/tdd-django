from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse('<html><title>Exercise</title><body><h1>Yogi Perdana</h1><h2>1906438115</h2></body></html>')