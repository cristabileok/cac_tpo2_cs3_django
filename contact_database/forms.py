from django.forms import ModelForm
from django import forms
from .models import Contact

class ContactForm(ModelForm):
    
    check = forms.BooleanField(required = True, label="Accepto compartir mis datos con CS3")
    
    class Meta:
        model = Contact        
        fields = [
            'name',
            'age',
            'sex',
            'email',
            'phone',
            'comunication',
            'reason',
            'message',            
            ]
        
        
