from django.shortcuts import render
from django.http import HttpResponse


def index_projet(request):
    #  return HttpResponse("<h1 style='text-align:center;'>Bienvenue au site de Master GLWA</h1>")
    return render(request, "base.html")

def contact(request):
    return render(request, 'pages/contact.html')

