#coding=utf8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from models import *
from forms import *
from django.views.generic import ListView,DetailView
from django.utils import timezone
def PublisherView(request):
    requesturl=request.get_host()
    return HttpResponse("Welcome to the page at %s" % request.is_secure())
def display_meta(request):
    values = request.META.items()
    #values.sort()
    html =[]
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, str(v).decode('gbk')))
    return HttpResponse('<table>%s</table>' % '\n'.join(html)+request.get_host())
def search_form(request):
    return render_to_response('search_form.html',context_instance=RequestContext(request))
def search(request):
    warn=[]
    if 'q' in request.POST:
        q = request.POST['q']
        if len(q) > 20:
            warn.append('too long')
        elif not q:
            warn.append('Please submit a search term')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_form.html',{'books': books, 'query': q,'res':books.exists(),'warn':warn},context_instance=RequestContext(request))
        return render_to_response('search_form.html',{'query': q,'warn':warn,'res':True},context_instance=RequestContext(request))
    elif 'q' not in request.POST:
        return render_to_response('search_form.html',{'res':True},context_instance=RequestContext(request))

def addbook(request):
    return render_to_response('addbook.html',{'form': bookForm},context_instance=RequestContext(request))
def addpublisher(request):
    publisherform=PublisherForm()
    return render_to_response('addpublisher.html',{'publisherform':publisherform},context_instance=RequestContext(request))
def delpublisher(request):
    id=request.GET['id']
    Publisher.objects.get(id=id).delete()
    return HttpResponseRedirect('/listpublisher/')
def updatepublisher(request):
    id=request.GET['id']
    publisherByid=Publisher.objects.get(id=id)
    return render_to_response('updatepublisher.html',{'publisherByid':publisherByid},context_instance=RequestContext(request))
def search_publisher_by_name(request):
    name=request.POST['name']
    publisherByname=Publisher.objects.filter(name__icontains=name)
    print '4444444444444'
    print publisherByname
    print '5555555555555'
    return render_to_response('listpublisher.html',{'publishers':publisherByname},context_instance=RequestContext(request))
def detailpublisher(request):
    id=request.GET['id']
    publisherByid=Publisher.objects.get(id=id)
    return render_to_response('detailpublisher.html',{'publisherByid':publisherByid},context_instance=RequestContext(request))
def listpublisher(request):
    publishers=Publisher.objects.all()
    return render_to_response('listpublisher.html',{'publishers':publishers},context_instance=RequestContext(request))
def savepublisher(request):
    print '####################'
    print request.POST
    print '*********************'
    publisherform=PublisherForm(request.POST)
    print '1111111111111'
    print publisherform
    print '2222222222222'
    publisher=Publisher()
    if publisherform.is_valid():
        if len(request.POST['id'])>0:
            publisher.id=request.POST['id']
        publisher.name=publisherform.cleaned_data['name']
        publisher.address=publisherform.cleaned_data['address']
        publisher.city=publisherform.cleaned_data['city']
        publisher.state_province=publisherform.cleaned_data['state_province']
        publisher.country=publisherform.cleaned_data['country']
        print publisher.country
        publisher.country = str(publisher.country).replace('u\'','\'')  
        publisher.country=publisher.country.decode("unicode-escape")
        publisher.website=publisherform.cleaned_data['website']
        publisher.last_accessed=publisherform.cleaned_data['last_accessed']
        publisher.save()
        return HttpResponseRedirect('/listpublisher/')
    return render_to_response('addpublisher.html',{'publisherform':publisherform},context_instance=RequestContext(request))
def addauthor(request,name):
    if request.method=='POST':
        authorForm=AuthorForm(request.POST)
        if authorForm.is_valid():
            first_name=authorForm.cleaned_data['first_name']
            last_name=authorForm.cleaned_data['last_name']
            email=authorForm.cleaned_data['email']
            last_accessed=authorForm.cleaned_data['last_accessed']
            Author(first_name=first_name,last_name=last_name,email=email,last_accessed=last_accessed).save()
            return HttpResponseRedirect('/addauthor/11/')
        return render_to_response('addauthor.html', {'authorform':authorForm,'name':name},context_instance=RequestContext(request))
    else:
        authorForm=AuthorForm()
        return render_to_response('addauthor.html', {'authorform':authorForm},context_instance=RequestContext(request))
def about_pages(request,n):
    #try:
    return render_to_response('about/%s.html' % n,context_instance=RequestContext(request))
    #except TemplateDoesNotExist:
     #   raise Http404()
    
class PublisherList(ListView):
    #model = Publisher
    context_object_name = 'my_favorite_publishers'
    queryset = Publisher.objects.filter(name='234')
class PublisherDetail(DetailView):
    model = Publisher
    context_object_name = 'my_favorite_publisher_detail'
    def get_context_data(self,**kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = Book.objects.all()
        return context
        queryset = Author.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(PublisherDetail, self).get_object()
        # Record the last accessed date
        object.last_accessed = timezone.now()
        object.save()
        # Return the object
        return object
class AcmeBookList(ListView):
    context_object_name = 'book_list'
    queryset = Book.objects.filter(publisher__name='1111')#多表查询
    template_name = 'books/acme_list.html'
from django.views.generic.edit import FormView,CreateView,UpdateView

class AuthorView(FormView):
    template_name = 'books/AuthorView.html'
    form_class = AuthorForm
    success_url = '/listpublisher/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.a()
        print '1111111111111111'
        return super(AuthorView, self).form_valid(form)
class AuthorCreate(CreateView):
    model = Author
    #fields = '__all__'
    template_name='books/addauthornew.html'
    success_url = '/AuthorList/'
class AuthorList(ListView):
    model = Author
    queryset = Author.objects.all()
    #context_object_name = 'author_list'
    #template_name='books/publisherlist.html'
class AuthorUpdate(UpdateView):
    model = Author
    template_name_suffix = '_update_form'
    def get(request, *args, **kwargs):
        id=request.id

# Create your views here.