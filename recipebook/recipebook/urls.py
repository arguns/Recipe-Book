"""recipebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vege.views import *
from home.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home,name="home"),
    path('admin/', admin.site.urls),
    path('recipes/', recipes, name="recipes"),
    path('delete-recipe/<id>/', delete_recipe, name="delete_recipe"),
    path('update-recipe/<id>/', update_recipe, name="update_recipe"),
    path('login/', user_login, name="user_login"),
    path('register/', user_register, name="user_register"),
    path('delete-user/<id>', user_del, name="user-delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    