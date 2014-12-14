#coding=utf-8
from django import forms
from models import user 

#继承forms.Form
'''
class userForm(forms.Form): 
    name = forms.CharField(label=(u"名称"),max_length=10,required=True,widget=forms.TextInput(attrs={'size': 20,})) 
    password = forms.CharField(required=True)
'''
'''
class userForm(forms.ModelForm):
    name_choice = ( 
    ('', u"---------"), 
    (2, u"2"),         
    (4, u"4"),         
    (8, u"8"), 
    (16, u"16"),)
    name = forms.ChoiceField(label=(u"昵称"),required=True, widget=forms.RadioSelect,choices=name_choice) 
    class Meta:
        model=user
        fields=('name','password')
'''
class userForm(forms.ModelForm): 
    class Meta: 
        model = user
        fields=('name','password')