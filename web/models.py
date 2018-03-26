
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

class Contact(models.Model):
	
	name        = models.CharField(max_length=128)
	company     = models.CharField(max_length=128)
	telephone   = models.IntegerField()
	email       = models.EmailField()
	message     = models.TextField(null=True,blank=True)

	class Meta:
		db_table            = 'contact'
		verbose_name        =_('contact')
		verbose_name_plural =_('contacts')
		ordering            = ('name',)


class Subscribe(models.Model):
	
	email = models.EmailField()
	

	class Meta:
		db_table            = 'subscribe'
		verbose_name        =_('subscribe')
		verbose_name_plural =_('subscribes')
		ordering            = ('email',)
