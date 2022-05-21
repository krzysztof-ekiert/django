from django.shortcuts import render
from django.http import HttpResponse

def biblioteka(request):
    return HttpResponse("Tu będzie moja biblioteka")