from multiprocessing import context
from django.shortcuts import render
from .forms import InputForm0, InputForm1,InputForm2,InputForm3,InputForm4


def form0(request):
    context={}
    if request.method=="POST":
        form=InputForm0(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data["name"],data["family"],data["age"],data["is_active"])
        else:
            context["error_message"]="Form not Valid...."
    else:
        form=InputForm0()
    context["form"]=form        
    return render(request,"formtest/form0.html",context)

#=================================================================================
def form01(request):
    context={}
    if request.method=="POST":
        form=InputForm0(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data["name"],data["family"],data["age"],data["is_active"])
        # else:
        #     context["error_message"]="Form not Valid...."
    else:
        form=InputForm0()
    context["form"]=form        
    return render(request,"formtest/form01.html",context)














#===================================================

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
    return render(request,"formtest/form3.html",context)



 
def form3(request):
    form=InputForm2()
    context={
        'form':form
        
    }
    return render(request,"formtest/form3.html",context)


def form4(request):
    form=InputForm4()
    context={
        'form':form
        
    }
    return render(request,"formtest/form4.html",context)



 
def form5(request):
    context={}
    if request.method=="POST":
        form=InputForm1(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            print(data["name"],data["family"],data["age"],data["is_active"])
        # else:
        #     context["error_message"]="Form not Valid....add"
    else:
        form=InputForm1()
    context["form"]=form        
    
    return render(request,"formtest/form5.html",context)







# def form6(request):
#     form=InputForm3()
#     context={
#         'form':form
        
#     }
#     return render(request,"formtest/form.html",context)