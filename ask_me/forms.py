from django import forms
from .models import Questions

class ContactForm(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ['username', 'mail', 'subject', 'question']

