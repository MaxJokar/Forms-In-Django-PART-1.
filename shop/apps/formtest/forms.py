from django import forms


class InputForm0():
    name=forms.CharField(max_length=10 , required=True)
    family=forms.CharField(max_length=15, label="Family")
    age=forms.IntegerField(label="Age",label_suffix="=>")
    is_active=forms.BooleanField(initial=True)