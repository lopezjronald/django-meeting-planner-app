from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from meetings.models import Meeting


def welcome(request):
    return render(request,
                  "website/welcome.html",
                  {"meetings": Meeting.objects.all()},)


def date(request):
    return HttpResponse(f"This page was served at {str(datetime.now())}")


def about(request):
    age = 34
    return HttpResponse(f"I am a {age} year old developer!")