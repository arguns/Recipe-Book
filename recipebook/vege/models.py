from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='img')
    recipe_view_count = models.IntegerField(default=1)

class Department(models.Model):
    pass

class Student(models.Model):
    
    student_name = models.TextField()