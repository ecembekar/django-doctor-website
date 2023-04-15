from django.shortcuts import render,redirect
from .models import Questions
from django.http import HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.is_public = False
            print("kaydedildi")
            question.publish = True
            question.save()
            messages.success(request,"Sorunuz Kaydedildi. Teşekkürler!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META['HTTP_REFERER'])
