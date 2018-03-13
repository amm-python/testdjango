#coding:utf-8
# Create your views here.

from django.http import HttpResponse
from app import models
from app.models import person
from django.shortcuts import render
import requests

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

def joke(request):
    haha_url = 'http://www.haha.mx/mobile_read_api.php?r=mobile_joke&type=hot&pn=1&pagesize=20&_=1520933252089'
    json_data = requests.get(haha_url).json()
    return render(request,"joke.html",{"list":json_data})