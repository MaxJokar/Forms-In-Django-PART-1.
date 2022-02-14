from audioop import avg
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