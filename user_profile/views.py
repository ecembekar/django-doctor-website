from django.shortcuts import render
from .models import Profile,Education,Experience,Publications,Operations,Specialization
from ask_me import models

# Create your views here.

def index(request):
    profiles = Profile.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    publications = Publications.objects.all()
    operations = Operations.objects.all()
    specializations = Specialization.objects.all()
    questions = models.Questions.objects.all() 

    context = {
        "profiles" : profiles,
        "educations" : educations,
        "experiences" : experiences,
        "publications" : publications,
        "operations" : operations,
        "specializations" : specializations,
        "questions" : questions,
    }

    return render(request,'index.html', context)

def about(request):
    return render(request, 'about.html')

def detail(request,id):
    publications = Publications.objects.filter(id = id)
    return render(request,"publication-details.html",{"publications" : publications})


