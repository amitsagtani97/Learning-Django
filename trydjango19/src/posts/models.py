from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length = 120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=False,auto_now_add=True)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

	def __unicode__(self):
		return self.title