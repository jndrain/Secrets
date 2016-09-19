from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Secret(models.Model):
    secret = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    comment = models.CharField(max_length=500)
    secret = models.ForeignKey(Secret)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
