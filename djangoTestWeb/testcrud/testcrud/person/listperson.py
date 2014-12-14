from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
def listPerson(req):
    t=get_template('../templates/1.html')
    html = t.render(Context({'current_date':'17:50'}))
    return HttpResponse(html)