#coding:utf-8
# Create your views here.

from django.http import HttpResponse
from app import models
from app.models import person
from django.shortcuts import render

def index(request):
    return HttpResponse("hello,this is my page.--amm")

def show(request):
    name = request.GET.get('name','')
    mark = request.GET.get('mark','')

    if name and mark:
        persons = models.person.objects.filter(name=name)
        if persons:
            persons.update(info=mark)
        else:
            person_new = person(name=name,age=1,info=mark)
            person_new.save()
    persons = models.person.objects.all();
    return render(request,"show.html",{"list":persons})