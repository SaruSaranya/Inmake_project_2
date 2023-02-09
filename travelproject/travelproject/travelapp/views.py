from django.shortcuts import render
from .models import Place,Team


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'teams':obj1})
# def demo1(request):
#     objs=Team.objects.all()
#     return render(request,"index.html",{'teams':objs})
