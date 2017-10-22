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