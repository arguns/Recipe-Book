from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *

# Create your views here.

def recipes(request):

    if request.method=="POST":
        data = request.POST

        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        Recipe.objects.create(
            recipe_image = recipe_image,
            recipe_name = recipe_name,
            recipe_description = recipe_description,
        )
 
        return redirect('/recipes/')

    queryset = Recipe.objects.all()
    context = {'page':'Recipe', 'Recipes':queryset}
    return render(request, 'recipes.html', context)

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()

    return redirect('/recipes/')

def update_recipe(request, id):

    queryset = Recipe.objects.get(id=id)
    context={'recupdate':queryset}

    if request.method=="POST":
        data = request.POST

        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description

        if recipe_image:
            queryset.recipe_image = recipe_image
        
        queryset.save()

        return redirect('/recipes/')
    return render(request,'update.html', context)



def user_login(request):

    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,"invalid username")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request,'Invalid Account')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/recipes/')
    else:
        queryset = User.objects.all()
        return render(request, 'login.html',context={'lists':queryset})


def user_register(request):

    if request.method == "POST":
        
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        username = request.POST.get('Username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username alraedy Exists')
            return redirect('/register/')


        user = User.objects.create(
            first_name = firstName,
            last_name = lastName,
            username = username,
            password = password
        )
        user.set_password(password)
        user.save()


        return redirect('/register/')

    queryset = User.objects.all()
    return render(request, 'register.html', context={'lists':queryset})

def logout_page(request):
    logout(request)
    return('/login')

def user_del(request,id):

    user = User.objects.get(id=id)
    user.delete()

    return redirect('/register/')
