from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_syllabus_tracker(request):
    return HttpResponse("Welcome to homepage of syllabus tracker")