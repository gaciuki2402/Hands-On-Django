from django.shortcuts import render
from polls.models import person
# Create your views here.

def Homeview(request):
    personQs=person.objects.all()
    context={
        "person":personQs
    }
    return render(request,"polls/home.html",context)