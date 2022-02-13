from django.shortcuts import render
from .forms import InputForm0
# from django.http import HttpResponse,Http404
# from django.conf import settings
# # from apps.blog.models import Author
# from .models import Author



def form(request):
    return render(request,"formtest/form.html")


def form0(request):
    form=InputForm0()
    context={
        'form':form
        
    }
    return render(request,"fomtest/form0.html")





    
# def index(request):
#     authors=Author.objects.all() # load all  datas in our table 
#     context={
#             'media_url':settings.MEDIA_URL,
#             "imagename":'th1.jfif',
#             'authors':authors
#             # 'blogList':blogList,
            
        
#         }

#     return render(request,'blog/index.html',context)

    
    
    
# def showAuthors(request):
#     authors=Author.objects.all() # load all  datas in our table 
#     context={
#             'media_url':settings.MEDIA_URL,
#             # "imagename":'th1.jfif',
#             'authors':authors
#             # 'blogList':blogList,
            
        
#         }
 
#     return render(request,'blog/authors.html',context)


# To have additional information about the  Tutor we can  use  Description section which one href  opens it . 

# def authorDetail(request,author_id):
#     try:
        
#         author=Author.objects.get(id=author_id)
#     except Author.DoesNotExist:  
#             raise Http404("This Page Does not Exit TTTTT")  
#     context={
#                 'media_url':settings.MEDIA_URL,
            
#                 'author':author
            

            
#             }
        
#     return render(request, 'blog/author_detail.html',context)








 