from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home (request):
    return render (request,'generator/home.html')
def about (request):
    return render (request,'generator/about.html')


def password(request):
    characters=list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get("верхний регистр"):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get("знаки"):
        characters.extend(list('!"#$%&\'\(\)*+,-./:;<=>?@[\]^_`{|}~'))
    if request.GET.get("цифры"):
        characters.extend(list('0123456789'))



    lenht=int(request.GET.get('длина',12))
    thepassword=''
    for x in range(lenht):
        thepassword+= random.choice(characters)
    return render (request,'generator/password.html',{'password': thepassword})
