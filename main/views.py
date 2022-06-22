from django.shortcuts import render, redirect
from .models import Block, BlockImage, FeedBack
from django.http import HttpResponseRedirect
from django.views.generic import View
from .forms import FeedBackForm
from django import forms


def index(request):

    context = {}
    context['blocks'] = Block.objects.all()

    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        
        if form.is_valid():
            feedback = form.save(commit=False)
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            feedback.name = name
            feedback.phone = phone
            feedback.email = email
            feedback.save()
            return HttpResponseRedirect('/') 
        else:
            context['form'] = form
            return render(request, 'main/index.html', context)
            
         
    else:
        #print(1)
        context['form'] = FeedBackForm()
        for i in context['form']:
            print(i)
        #print(request)
        
        return render(request, 'main/index.html', context)
