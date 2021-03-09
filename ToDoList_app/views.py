from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    activity=Activity.objects.all()
    form=ActivityForm()
    if request.method=='POST':
        form=ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'activity':activity,'form':form}
    return render(request,'liste/liste_form.html',context)