from django.shortcuts import render
from .models import *
from django.forms.models import modelform_factory
from django.shortcuts import get_object_or_404
from .forms import messageForm
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import authenticate, login


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
    club=get_object_or_404(Club, id=clubId)
    messages=Message.objects.filter(chat_room=club)
    messages_not_replies = [m for m in messages if not hasattr(m,'replymessage')]
    replies=ReplyMessage.objects.filter(chat_room=club)
    form = messageForm()
    context={
        'club':club,
        'messages':messages_not_replies,
        'replies':replies,
        'form':messageForm,
    }

    return render(request,'club_page.html',context)


def postNewMessage(request,club_id):
    if request.user.is_authenticated():
        form = messageForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['mesaj']
            new_m = Message.objects.create(yazan_id=request.user.id, chat_room_id=club_id, mesaj=message)
            new_m.save()
    return HttpResponseRedirect('/mezunlar/clubs/'+club_id)


def postNewReply(request,club_id,main_m_id):
    print('new reply initiated')
    if request.user.is_authenticated:
        print('user in')
        form = messageForm(request.POST)
        if form.is_valid():
            print('form valid')
            message = form.cleaned_data['mesaj']
            new_r = ReplyMessage.objects.create(yazan_id=request.user.id, chat_room_id=club_id, mesaj=message,main_id=main_m_id)
            new_r.save()
            print('message save is pased')
    return HttpResponseRedirect('/mezunlar/clubs/'+club_id)