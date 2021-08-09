from django import forms
from .models import Todo

class MessageForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ['content']