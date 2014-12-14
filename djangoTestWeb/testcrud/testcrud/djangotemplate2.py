#coding=utf8
from django.template import Template, Context
from django.conf import settings
settings.configure()
person={'username':'auuppp','password':'123456'}
t=Template('username is {{a.username}},password is {{a.password}}')
c=Context({'a':person})
print t.render(c)

age=30
cc=Context({'age':age})
tt=Template('age is {{age}}')
print tt.render(cc)

class testtemplate(object):
    username='auuppp2'
    def getusername(self):
        return self.username
    def setusername(self,p=1):
        return p
    def deleteusername(self):
        self.username='auuppp3'
        return self.username
    #deleteusername.alters_data = True
testte=testtemplate()
#print testte.getusername()
ccc=Context({'a':testte})
#属性查找
tt1=Template('username is {{a.username}}')
#方法调用
ttt=Template('username is {{a.getusername}}')
#方法调用
tttt=Template('username is {{a.setusername}}')
ttttt=Template('username is {{a.deleteusername}}')
t5=Template('username is {{a.deleteusername1}}')
print tt1.render(ccc)
print ttt.render(ccc)
print tttt.render(ccc)
print ttttt.render(ccc)
print t5.render(ccc)
