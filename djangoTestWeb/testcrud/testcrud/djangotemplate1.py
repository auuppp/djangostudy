from django.template import Template, Context
from django.conf import settings
print settings.configure()

class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name, self.last_name = first_name, last_name
t = Template('Hello, {{ person.first_name }} {{ person.last_name }}.')
c = Context({'person': Person('John', 'Smith')})
print t.render(c)
