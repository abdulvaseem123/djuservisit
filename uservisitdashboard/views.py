from django.shortcuts import render
from django.http import HttpResponse
from .models import UserVisit

def index(request):
    all_users=UserVisit.objects.all()
    context={'all_users':all_users}
    return render(request,'uservisitdashboard/index.html',context)

