from audioop import avg
from logging import PlaceHolder
from django import forms


class InputForm1(forms.Form):
    name=forms.CharField(max_length=10 , required=True,label='Name')
    family=forms.CharField(max_length=15, label="Family")
    age=forms.IntegerField(label="Age",label_suffix="=>")
    is_active=forms.BooleanField(initial=True)
    
        
class InputForm2(forms.Form):
    name=forms.CharField(max_length=10 , required=True,label='Name')
    family=forms.CharField(max_length=15, label="Family")
    age=forms.IntegerField(label="Age",label_suffix="=>")
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
    
     
    
         
class widgetForm1(forms.Form):
    name=forms.CharField(
        max_length=10 , 
        required=True,
        label='Name',
        widget=forms.TextInput(attrs={'class':'c1','placeholder':'ENTER You Name'}))
    
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
    
    
    