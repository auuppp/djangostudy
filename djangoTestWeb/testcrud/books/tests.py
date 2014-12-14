from django.conf import settings
settings.configure()

#import os
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testcrud.settings")
from models import Publisher,Book
#import os
#import sys
#sys.path.append("D:\\testing\\python\\djangoTestWeb\\testcrud")
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testcrud.settings")
b1=Book(title='title',publisher_id='1111111',publication_date='2014-09-09')
p1 = Publisher(name='Apress111222', address='2855 Telegraph Avenue',city='Berkeley',state_province='CA', country='U.S.A.',website='http://www.apress.com/')
#p1.save()
p2=Publisher.objects.all()
#print p2
#P3=Publisher.objects.get(name="Apress111222")
#Publisher.objects.filter(name='Apress')
#Publisher.objects.filter(name__contains="press")
Publisher.objects.order_by("name")
Publisher.objects.order_by("-name")
a=Publisher.objects.order_by('name')[0:2]
print type(a)
#Publisher.objects.order_by('name')[0]

#Publisher.objects.order_by('name')[0:2]
#Publisher.objects.filter(id=6).update(name='1111111')Publisher.objects.filter(id=6).update(name='1111111')
'''
p=Publisher.objects.get(name='Apress')
p.name = 'Apress Publishing'
p.save()
'''
'''
p = Publisher.objects.get(name="1111111")
p.delete()
'''
#Publisher.objects.filter(country='Apress111').delete()