from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject

# Create your views here.
def home_syllabus_tracker(request):
    subjects = Subject.objects.all()
    return render(request,'syllabus_overview.html',{'subjects': subjects} )

