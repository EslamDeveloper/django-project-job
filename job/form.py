from dataclasses import Field, fields
from pyexpat import model
from django import forms

from .models import Apply , job

class ApplyForm(forms.ModelForm):
    class  Meta:
       model = Apply
       fields = ['name' ,'email','webiste','cv','cover_letter']
       

class jobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'
        exclude =('owner','sulg')