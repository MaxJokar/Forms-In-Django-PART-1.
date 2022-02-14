from django.shortcuts import render
from .forms import InputForm1,InputForm2



def form(request):
    return render(request,"formtest/form.html")





def form1(request):
    form=InputForm1()
    context={
        'form':form
        
    }
    return render(request,"formtest/form1.html",context)




def form2(request):
    form=InputForm2()
    context={
        'form':form
        
    }
    return render(request,"formtest/form2.html",context)



 