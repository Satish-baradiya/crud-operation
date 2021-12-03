from django.shortcuts import render
from django.http import HttpResponse 
from .models import Data
from .forms import DataForm
from django.shortcuts import  get_object_or_404,HttpResponseRedirect,render


# Create your views here.
def index(request):
    form = DataForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponse("data added ")
    return render(request,"crud/index.html",{
        "form":form
    })

def list_view(request):
    data = Data.objects.all()
    return render(request,"crud/view.html",{
        "data":data
    })


