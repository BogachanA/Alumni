from django.shortcuts import render
from .models import *
from django.forms.models import modelform_factory
from django.shortcuts import get_object_or_404
from .forms import messageForm

# Create your views here.


def graduates(request):
    graduateList=Alumni.objects.all()
    context={
        'graduateList':graduateList,
    }
    return render(request,'base.html',context)


def graduateInfo(request,id):
    alumni=get_object_or_404(Alumni,id=id)
    if request.method =="GET":
        message_create=messageForm()
    elif request.method == "POST":
        message_create=messageForm(request.POST)
        if message_create.is_valid():
            yazan=message_create.cleaned_data['yazan']
            mesaj = message_create.cleaned_data['mesaj']
            to=alumni
            Message.objects.create(yazan=yazan, to=to, mesaj=mesaj)
    all_messages=Message.objects.filter(to=alumni)
    context={
        'form':message_create,
        'graduate':alumni,
        'messages':all_messages,
    }
    return render(request,'grad_info.html',context)


def clubs(request):
    clubsList = Club.objects.all()
    context = {
        'clubs':clubsList,
    }
    return render(request,'clubs.html',context)


def clubPage(request,clubId):
    club=get_object_or_404(Club,id=clubId)
    messages=Message.objects.filter(chat_room=club)
    messages_not_replies= [m for m in messages if not hasattr(m,'replymessage')]
    context={
        'club':club,
        'messages':messages_not_replies,
    }
    return render(request,'club_page.html',context)