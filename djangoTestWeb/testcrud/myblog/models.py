#coding=utf-8
from django.db import models
class lagou(models.Model):
	"""docstring for ClassName"""
	name = models.CharField(max_length=30)
	class Meta:
	    app_label='myblog'
class user(models.Model):
    name=models.CharField(max_length=30,verbose_name='用户名')
    password=models.CharField(max_length=30,verbose_name='密码')
# Create your models here.