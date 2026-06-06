from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def place_list(request):
    return HttpResponse("Welcome to ExploreDuniya")