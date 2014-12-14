from django.template import Template,Context
from django.conf import settings
settings.configure()
t = Template('My name is {{ name }}.')
c = Context({'name': 'Stephane'})
print t.render(c)
#C:\Python27\DLLs;D:\testing\python\djangoTestWeb\testcrud