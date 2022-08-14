from django.shortcuts import render
from main.models import Block, FeedBack, BotUsers
from django.http import JsonResponse
from .forms import FeedBackForm

def start_bot(request):
    import os
    from aiogram import Bot, Dispatcher, executor
    from dotenv import load_dotenv
    load_dotenv()

    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher(bot)
    executor.start_polling(dp, skip_updates=True)

def create_block_dict_with_icons(context, tag):
    context[tag] = Block.objects.get(tag=tag)
    context[f'{tag}_list'] = [text.replace('\r', '') for text in context[tag].text.split('\n')]
    context[f'{tag}_dict'] = {}
    for key in context[f'{tag}_list']:
        context[f'{tag}_dict'][key] = f'/media/{key}.png'

def index(request):
    context = {}
    context['blocks'] = Block.objects.all()
    create_block_dict_with_icons(context, 'sites_add')
    create_block_dict_with_icons(context, 'sites_add')
    create_block_dict_with_icons(context, 'bots')
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
            from main.management.commands.commands import send_message
            from concurrent.futures import ThreadPoolExecutor
            from asyncio import run
            bot_mailing_list_recipients = BotUsers.objects.all()
            for user in bot_mailing_list_recipients:
                pool = ThreadPoolExecutor()
                pool.submit(run, send_message(user.userid, "Есть новая заявка!")).result()
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
