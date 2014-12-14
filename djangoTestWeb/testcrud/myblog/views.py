from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from forms import userForm
from models import user
from django.template import RequestContext
def testform(request):
    return render_to_response('form.html')
def search(request,id1,summary):
    dict11={}
    list1=[]
    if 'q' in request.GET:
        #print summary
        message = 'You searched for: %r' % request.GET['q']+summary+id1
        dict11={'username':'auuppp','password':'md5'}
        list1=['11','22','33']
    else:
        message = 'You submitted an empty form.'
    return render(request,'form.html',locals())
def adduserView(request):
    if request.method == 'POST': 
        form =userForm(request.POST) 
        if form.is_valid(): 
            username=form.cleaned_data['name']
            password=form.cleaned_data['password']
            user(name=username,password=password).save()
            return HttpResponseRedirect('/adduserView')
    else:
        form = userForm()
    return render_to_response('message.html', {'form':form},context_instance=RequestContext(request))
def listuser(request):
    #form=user.objects.all()
    a=user.objects.all()
    return render_to_response('listuser.html', {'form':a},context_instance=RequestContext(request))
def topView(request):
    title='gyp'
    return render_to_response('top.html',locals())
# Create your views here.