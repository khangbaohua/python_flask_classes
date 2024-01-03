from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def lalala(request):
    return render(request, "lalala.html")