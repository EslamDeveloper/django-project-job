from operator import mod
from random import choices
from turtle import title
from django.db import models

# Create your models here.
JOB_TYPE =( 
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

class job(models.Model): #table
    title = models.CharField(max_length=100) #coumn

    #location.........
    job_type = models.CharField(max_length=15, choices = JOB_TYPE)
