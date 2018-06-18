# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Docinfo(models.Model):
    foldername = models.CharField(max_length = 50)
    filename   = models.CharField(max_length = 50)
    iscomplete = models.CharField(max_length=10)
    iscorrect  = models.CharField(max_length=10)