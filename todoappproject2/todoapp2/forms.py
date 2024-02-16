from . models import Todotask
from django import forms

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todotask
        fields=['name','priority','date']