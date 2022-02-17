from audioop import avg
from dataclasses import fields
from distutils.command import clean
from logging import PlaceHolder
# from xml.dom import ValidationErr
from django import forms
from django.core.exceptions import ValidationError
from django.core  import validators
from .models import Post




def checkValidateName(value):
    value=str(value)
    if len(value)<2 or len (value)>20:
        raise forms.ValidationError("Name is Invalid(more than 2 less than 20 Char accepted)") 

def ageValidate(value):
     value=int(value)
     if value<18 or value>70:
         raise forms.ValidationError("Age Out of  Range ,less than 18 older than 70 not Accepted") 

class InputForm0(forms.Form):
    # name=forms.CharField(max_length=10 , required=True,label='Name')
    name=forms.CharField(max_length=10 , required=True,label='Name',validators=[checkValidateName])
    family=forms.CharField(max_length=15, label="Family")
    age=forms.IntegerField(label="Age",label_suffix="=>",validators=[ageValidate] )
    is_active=forms.BooleanField(initial=True)


    def clean_name(self):
        name=self.cleaned_data["name"]
        return name
    
    def clean_family(self):
        family=self.cleaned_data["family"]
        if family[0]=='A': 
            raise ValidationError(" Begining Letter With 'A'  NOT Accepted !")
        return family
    
    def clean_age(self):
        age=self.cleaned_data["age"]
        return age
    



class InputForm(forms.Form):
    name=forms.CharField(max_length=10 , required=True,label='Name')
    family=forms.CharField(max_length=15, label="Family")
    age=forms.IntegerField(label="Age",label_suffix="=>")
    is_active=forms.BooleanField(initial=True)
    

#===================================================================================

class InputForm1(forms.Form):
    name=forms.CharField(max_length=10 , required=True,label='Name')
    family=forms.CharField(max_length=15, label="Family")
    age=forms.IntegerField(label="Age",label_suffix="=>")
    is_active=forms.BooleanField(initial=True)
    
#===================================================================================    
   
def checkValidateName(value):
    value=str(value)
    if len(value)<3 or len (value)>20:
        raise forms.ValidationError("Name is INvalid") 
    
def ageValidate(value):
     value=int(value)
     if value<18 or value>70:
         raise forms.ValidationError("Age Out of  Range") 
        
class InputForm2(forms.Form):
    name=forms.CharField(max_length=10 , required=True,label='Name',validators=[checkValidateName])
    family=forms.CharField(max_length=15, label="Family")
    age=forms.IntegerField(label="Age",label_suffix="=>",validators=[ageValidate])
    is_active=forms.BooleanField(initial=True)
    avg=forms.DecimalField(max_digits=4,decimal_places=2,label="Score Average")
    email=forms.EmailField(max_length=50,label="email")
    register_date=forms.DateField(label="Date of Enrolment")
    url=forms.URLField(label="WebSite Address")
    image=forms.ImageField(label="Image")
    FAVORITE_COLOR=[
                    ("1","Red"),
                    ("2","Green"),
                    ("3","Blue"),
                    ("4","Yellow"),                             
                    ]
    color=forms.ChoiceField(choices=FAVORITE_COLOR)
    colors=forms.MultipleChoiceField(choices=FAVORITE_COLOR)
    
  #check data given from the User    
    def clean_name(self):
        name=self.cleaned_data["name"]
        return name
    
    def clean_family(self):
        family=self.cleaned_data["family"]
        if family[0]!='A': 
            raise ValidationError("Family Must not started by  A...")
        return family
    
    def clean_age(self):
        age=self.cleaned_data["age"]
        return age
    

#===================================================================================       



class InputForm3(forms.Form):
    name=forms.CharField(max_length=10 , required=True,label='Name')    
    family=forms.CharField(max_length=15, label="Family")
    password=forms.CharField(max_length="10",label="PASSWORD",widget=forms.PasswordInput)
    Year_Choice=['2018','2019','2020','2021','2022'] #Limited years  Added 
    register_date1=forms.DateField(label="Date of Enrolment", required=False,widget=forms.SelectDateWidget(years=Year_Choice))
    register_date2=forms.DateField(label="Date of Enrolment", required=False,widget=forms.NumberInput(attrs={'type':'date'}))
    #attribute added to show its type of  date.anytime we wanted a property and a tag added to html ,use attrs
    FAVORITE_COLOR=[
                    ("1","Red"),
                    ("2","Green"),
                    ("3","Blue"),
                    ("4","Yellow"),                             
                    ]
    color=forms.ChoiceField(choices=FAVORITE_COLOR)
    colors=forms.MultipleChoiceField(choices=FAVORITE_COLOR)
    description=forms.BooleanField(widget=forms.Textarea)
    description.widget.attrs.update({'class':'c1'})
    

#===================================================================================         
    
def checkValidateName(value):
    value=str(value)
    if len(value)<2 or len (value)>20:
        raise forms.ValidationError("Name is INvalid") 
    
    
# def ageValidate(value):
#      value=int(value)
#      if value<18 or value>70:
#          raise forms.ValidationError("Age Out of  Range")
     
    
class InputForm4(forms.Form):
    name=forms.CharField(max_length=10 , required=True,label='Name', validators=[checkValidateName])    
    family=forms.CharField(max_length=15, label="Family")
    age=forms.IntegerField(label="Age",validators=[validators.MaxLengthValidator(40,message="Out of 40 is not accepted"),validators.MinLengthValidator(20)])
    # age=forms.IntegerField(label="Age",validators=[ageValidate])
    is_active=forms.BooleanField(initial=True)
    
    def clean_name(self) :
        name=self.cleaned_data["name"]
        return name
    
    def clean_family(self) :
        family=self.cleaned_data["family"]
        if family[0]!='A': 
            raise ValidationError("Family Must not started by  A...")
        return family
    
    def clean_age(self) :
        age=self.cleaned_data["age"]
        return age
    
class InputForm6(forms.ModelForm):
    class Meta:
        model=Post
        fields="__all__" #This wasy django takes all fields from Model post ,and make the class InputFom6  (no need again represent one by one)
        # fields=['title','Description']
    
    
    

    
 
    
    
    
     
    
    
    
    
    
    
    
    
    