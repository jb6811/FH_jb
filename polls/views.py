from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'polls/home.html')

def highscore(request):
    return render(request, 'polls/highscore.html')