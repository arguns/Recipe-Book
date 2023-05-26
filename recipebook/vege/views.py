from django.shortcuts import render, redirect
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

    return render(request, 'login.html')


def user_register(request):

    return render(request, 'register.html')