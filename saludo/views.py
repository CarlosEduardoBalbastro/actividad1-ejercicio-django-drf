from django.shortcuts import render

from django.http import HttpResponse

def decir_hola(request):
    return HttpResponse("¡Hola, mundo de Django!")
