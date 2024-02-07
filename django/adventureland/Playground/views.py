from django.shortcuts import render
from . models import Toy
def playground(request):
   Playgrounds = Toy.objects.all()
   data={

      "Playgrounds":Playgrounds
   }
   return render(request,"playground.html", data) 






# Create your views here.
