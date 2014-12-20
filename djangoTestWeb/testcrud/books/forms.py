#coding=utf-8
from django import forms
from models import Book,Publisher
from django.contrib.admin import widgets
class bookForm(forms.ModelForm): 
    class Meta: 
        model = Book
        fields = ('title','authors', 'publisher','publication_date')
class PublisherForm(forms.Form):
    country = (("中国", "中国"), ("美国", "美国"))
    state_province=(("北京","北京"),("上海","上海"))
    name=forms.CharField(label='名字')
    address=forms.CharField(label='地址')
    city=forms.CharField(label='城市')
    state_province=forms.ChoiceField(label='省份',choices=state_province)
    country=forms.MultipleChoiceField(label='国家',choices=country, widget=forms.SelectMultiple())
    website=forms.URLField(label='网址')
    last_accessed=forms.DateField(label='日期',widget=widgets.AdminDateWidget())
class AuthorForm(forms.Form):
    first_name=forms.CharField(label='姓',max_length=10,error_messages={'required': '你这个无姓人士.....'})
    last_name=forms.CharField()
    email=forms.EmailField()
    last_accessed=forms.DateTimeField(label='日期',widget=widgets.AdminDateWidget())
    def a(self):
    	print '11'
