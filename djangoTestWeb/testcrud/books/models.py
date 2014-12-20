#coding=utf8
from django.db import models
#https://docs.djangoproject.com/en/dev/topics/migrations/
class PublisherManager(models.Manager):
    def name_count(self, keyword):
        return self.filter(name__icontains=keyword).count()
class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='用户名')
    address = models.CharField(max_length=50,verbose_name='地址')
    city = models.CharField(max_length=60,verbose_name='城市')
    state_province = models.CharField(max_length=30,verbose_name='省份')
    country = models.CharField(max_length=50,verbose_name='国家')
    website = models.URLField(blank=True,null=True,verbose_name='网址')
    last_accessed=models.DateField(verbose_name='最后访问日期')
    objects=PublisherManager()
    class Meta:
        app_label = 'books'
    def __unicode__(self):
        return '%s %s' % (self.name,self.city)

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    last_accessed = models.DateTimeField()
    class Meta:
        app_label = 'books'

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    class Meta:
        app_label = 'books'
    def __unicode__(self):
        return self.title