from django.urls import path,re_path
import apps.formtest.views as views 


urlpatterns = [
    path('form/',views.form),
    path('form0/',views.form0),
    
]







# from django.urls import path , settings , include
# import apps.blog.views as views , admin
# from django.conf.urls.static import static
            
# urlpatterns = [
     # path('',views.index),
     # path('authors',views.showAuthors),
     # path('author/<int:author_id>',views.authorDetail),
     # path('formtest/',include('apps.formtest.urls')),
    
    
# ]+static(settings.MEDIA_URL,document_root=settings.MEDIAROOT)  
# admin.site.site_header='Manager Panel'
# admin.site.index_title='WELCOME TO MANAGER PANEL'         