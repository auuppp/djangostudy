#coding=utf-8
from django import template
from django.conf import settings
import sys
settings.configure()
reload(sys)  
sys.setdefaultencoding('utf8')  
tem=template.Template('my name is {{num}}')
con=template.Context({'num':'测试'})
print tem.render(con)

dict1={'name':'auuppp','age':'30'}
tem=template.Template('{{person.name}}\'s age is {{person.age}}')
con=template.Context({'person':dict1})
print tem.render(con)
con1=template.Context({'key1':'values'})
print con1['key1']
del con1['key1']
