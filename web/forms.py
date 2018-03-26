from django import forms
from django.forms.widgets import TextInput,Textarea
from django.utils.translation import ugettext_lazy as _
from web.models import Contact, Subscribe
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
	class Meta : 
		model = Contact
		exclude = []
		widgets ={

		'name':TextInput(attrs={'placeholder' :'Name'}),
		'company':TextInput(attrs={'placeholder':'Company'}),
		'telephone': TextInput(attrs={'placeholder' : 'telephone'}),
        'email': TextInput(attrs={'placeholder': 'email'}),
        'message': Textarea(attrs={'placeholder' : 'type your query here'}),

		}


class SubscribeForm(forms.ModelForm):
    
    class Meta:
        model = Subscribe
        exclude = []
        widgets = {
            'email': TextInput(attrs={'placeholder': 'email'}),
            }