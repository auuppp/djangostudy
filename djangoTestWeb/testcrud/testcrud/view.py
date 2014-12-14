from django.http import HttpResponse
import datetime
def hello(req):
    return HttpResponse('<h1>hello world!<h1>'+req.META['REMOTE_ADDR'])
def homepage(req):
    return HttpResponse('this is homepage')
def ctime(req,num):
    try:
        num=int(num)
        num=str(num)
    except ValueError:
        raise Http404
    #cutime=datetime.datetime.now()
    txt='this is %s' % num
    return HttpResponse(txt)