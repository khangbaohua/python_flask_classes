from django.shortcuts import render



from . models import Item
def mytodo(request):
   mytodo = Item.objects.all()
   data={

      "mytodo":mytodo
   }
   return render(request,"mytodo.html", data) 





# Create your views here.
