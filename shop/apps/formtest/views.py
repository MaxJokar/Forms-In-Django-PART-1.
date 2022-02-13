from django.shortcuts import render
from .forms import InputForm1



def form(request):
    return render(request,"formtest/form.html")





def form1(request):
    forms=InputForm1()
    context={
        'form':forms
        
    }
    return render(request,"formtest/form1.html",context)








 