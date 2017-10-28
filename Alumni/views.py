from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login


def mainRedirect(request):
    return HttpResponseRedirect('/mezunlar/')



