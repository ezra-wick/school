from django.shortcuts import render, redirect
from .models import Block, BlockImage, FeedBack
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import View
from .forms import FeedBackForm
from django import forms


def index(request):

    context = {}
    context['blocks'] = Block.objects.all()
    context['sites_add'] = Block.objects.get(tag='sites-add')
    context['sites_add_list'] = [text.replace('\r', '') for text in Block.objects.get(tag='sites-add').text.split('\n')]
    context['sites_dict'] = {}
    for site_type in context['sites_add_list']:
        context['sites_dict'][site_type] = f'/media/{site_type}.png'
    
    context['programms'] = Block.objects.get(tag='programms')

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

def check_feeld(request):
    if request.method == 'POST':
        print(request.POST)
        phone = request.POST["phone"]
        email = request.POST["email"]
        print(email)
        if phone=='none' and email!='' and email!='none':
            print(FeedBack.objects.filter(email=email).exists())
            if not FeedBack.objects.filter(email=email):
                return JsonResponse({"status":"ok","error_email": ""}, status="200", safe=False, json_dumps_params={"ensure_ascii" : False})
            else:
                return JsonResponse({"status":"error","error_email": "Заявка с таким email уже существует!"}, status="200", safe=False, json_dumps_params={"ensure_ascii" : False})
        if email=='none' and phone!='' and phone!='none':
            if phone[0] == "8":
                phone2 = "+7" + phone[1:len(phone)]
            else:
                phone2 = "8" + phone[2:len(phone)]
            if (not FeedBack.objects.filter(phone=phone)) and (not FeedBack.objects.filter(phone=phone2)):
                return JsonResponse({"status":"ok","error_phone": ""}, status="200", safe=False, json_dumps_params={"ensure_ascii" : False})
            else:
                return JsonResponse({"status":"error","error_phone": "Заявка с таким телефоном уже существует!"}, status="200", safe=False, json_dumps_params={"ensure_ascii" : False})