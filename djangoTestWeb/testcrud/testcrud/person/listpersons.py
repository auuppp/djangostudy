from django.shortcuts import render_to_response
def listPerson(req):
    dict1={'current_date':'17:50','username':'auuppp'}
    age=30
    return render_to_response('../templates/1.html',{'dict1':dict1,'age':age})
def listPerson2(req):
    return render_to_response('../templates/2.html')