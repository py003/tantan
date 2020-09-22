from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def toUser(request):

    return HttpResponse('hello world!')