from django.contrib import admin
# from .models import Author
# Register your models here.


class AuthorAdmin(admin.ModelAdmin): 
    List_display=('name','family','email','age','register_date')
    list_filter=('family','is_active')# adding a filter to our Administration
    search_fields=('family',) #comma is VIP cuse its not considered as a list
    



# admin.site.register(Author,AuthorAdmin)