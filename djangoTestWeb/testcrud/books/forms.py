#coding=utf-8
from django import forms
from models import Book,Publisher
class bookForm(forms.ModelForm): 
    class Meta: 
        model = Book
        fields = ('title','authors', 'publisher','publication_date')
class PublisherForm(forms.ModelForm):
    class Meta:
        model=Publisher
        fields = "__all__"
class AuthorForm(forms.Form):
    first_name=forms.CharField(label='姓',max_length=10,error_messages={'required': '你这个无姓人士.....'})
    last_name=forms.CharField()
    email=forms.EmailField()
