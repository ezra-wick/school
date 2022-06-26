from django.shortcuts import render, redirect
from .models import Block, BlockImage, FeedBack
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import View
from .forms import FeedBackForm
from django import forms


def index(request):

    context = {}
    context['blocks'] = Block.objects.all()
    context['form'] = FeedBackForm()

    return render(request, 'main/index.html', context)




def check_form(request):
    context = {}
    if request.method == 'POST':
        context['form'] = FeedBackForm(request.POST)
        if context['form'].is_valid():
            context['form'].save()
            # name = form.cleaned_data['name'] ЗДЕСЬ ЭТО НЕ НУЖНО. НО В ДРУГИХ СИТУАЦИЯХ МОЖЕТ БЫТЬ ПОЛЕЗНО
            # phone = form.cleaned_data['phone']
            # email = form.cleaned_data['email']
            # feedback.name = name
            # feedback.phone = phone
            # feedback.email = email
            # feedback.save()
            return JsonResponse({
                'status':'success'
            }
            )

        return render(request, 'includes/ajax_form_part.html', context)
