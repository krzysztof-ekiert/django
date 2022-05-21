from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

def hello(request, text="Pindol"):
    return HttpResponse(f"Hello {text} CHUUUUUUUUUJ")

# /hello/<sent1>/<sent2> -> <h1>sen1 sent2</h1>
def custom_greetings(request, s1,s2):
    return HttpResponse(f"<h1>{s1}<br>{s2}</h1>")