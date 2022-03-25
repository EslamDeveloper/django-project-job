from ast import Delete
from distutils.command import upload
from email.mime import image
from email.policy import default
from importlib.abc import TraversableResources
from operator import mod
from random import choices
from tkinter import CASCADE
from turtle import title
from xml.dom.minidom import CharacterData
from django.db import models
from django.urls import set_urlconf
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
JOB_TYPE =( 
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance,filename):             
    imagename , extension = filename.split(".")    
    return "jobs/%s.%s"%(instance.id,extension)


class job(models.Model): #table
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100) #coumn
    #location.........
    job_type = models.CharField(max_length=15, choices = JOB_TYPE)
    description = models.TextField(max_length=1000)
    publinshed_at = models.DateTimeField(auto_now = True)
    vacancy = models.IntegerField(default = 1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default = 1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    image = models.ImageField(upload_to = image_upload)
    
    sulg = models.SlugField(blank=True, null= True)

    
    def save(self,*args, **kwargs):
        self.sulg = slugify(self.title)
        super(job,self).save(*args, **kwargs )

    def __str__(self):
        return self.title
    
    
class Category(models.Model): #Category
     name = models.CharField(max_length=25)

     def __str__(self):
         return self.name
     
     
     
##Hna Apply user.......
class Apply(models.Model):
    job = models.ForeignKey('job', related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    webiste = models.URLField(max_length=200)
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now = True)

    
    def __str__(self):
        return self.name