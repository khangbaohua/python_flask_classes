from django.shortcuts import render
from .models import Banana
def banana(request):
    bananas=Banana.objects.all()
    data={
        "bananas":bananas
    }
    return render(request,"banana.html",data)
# Create your views here.
