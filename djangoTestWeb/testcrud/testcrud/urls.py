from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from books.views import *
#from myblog.views import *
#from testcrud.view import *
#from testcrud.person.listpersons import *
urlpatterns=patterns('books.views',
    url(r'^PublisherView/$', 'PublisherView'),
    url(r'^display_meta/$', 'display_meta'),
    url(r'^search_form/$', 'search_form'),
    url(r'^search/$','search'),
    url(r'^addbook', 'addbook'),
    url(r'^addpublisher/$', 'addpublisher'),
    url(r'^savepublisher/$', 'savepublisher'),
    url(r'^addauthor/(?P<name>.*)/$', 'addauthor'),
    url(r'^listpublisher/$', 'listpublisher'),
    url(r'^delpublisher', 'delpublisher'),
    url(r'^updatepublisher', 'updatepublisher'),
    url(r'^detailpublisher','detailpublisher'),
    url(r'^search_publisher_by_name/$','search_publisher_by_name'),
    url(r'^publishers/$',PublisherList.as_view()),
    #url(r'^publisherDetail/(?P<pk>\w+)/$',PublisherDetail.as_view()),
    url(r'^publisherDetail/(?P<pk>\w+)/$',PublisherDetail.as_view()),
    url(r'^AcmeBookList/$', AcmeBookList.as_view()),
    url(r'^AuthorView/$', AuthorView.as_view()),
    url(r'^AuthorCreate/$',AuthorCreate.as_view()),
    url(r'^AuthorList/$', AuthorList.as_view()),
    url(r'^AuthorUpdate/(?P<pk>\w+)/$', AuthorUpdate.as_view()),
)
urlpatterns+= patterns('myblog.views',
    url(r'^testform/$', 'testform'),
    url('^search/(?P<id1>[^/]+)/$', 'search',{'summary': '1'},name='names'),
    url(r'^adduserView/$', 'adduserView'),
    url(r'^listuser/$','listuser'),
    url(r'^topView/$','topView'),
    
)
urlpatterns+=patterns('testcrud.view',
    url(r'^hello/$','hello'),
    url('^$', 'homepage'),
    url(r'^ctime/(\d{1,2})/$', 'ctime'),
)
urlpatterns+=patterns('testcrud.person.listpersons',
    url(r'^listperson/$', 'listPerson'),
    url(r'^listperson2/$', 'listPerson2'),
)
def i18n_javascript(request):
    return admin.site.i18n_javascript(request)
urlpatterns+=patterns('',
    url(r'^admin/jsi18n', i18n_javascript),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^about/(\w+)/$', 'books.views.about_pages'),
)
urlpatterns+= patterns('',
    url(r'^about/$',TemplateView.as_view(template_name="about.html")),
    url(r'^about/(\w+)/$', 'books.views.about_pages'),
)
urlpatterns+=patterns('',
    (r'^static/(?P<path>.*)$','django.views.static.server',
        {'document_root':settings.STATICFILES_DIRS, 'show_indexes': True}),
)