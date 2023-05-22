from django.shortcuts import render

# Create your views here.


def home(request):
    context= {'page':'Home'}
    return render(request, "home.html",context)