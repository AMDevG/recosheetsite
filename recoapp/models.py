# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class Attachment(models.Model):
    
    file_name = models.CharField(max_length=100)
    attachment = models.FileField(upload_to='documents/%Y/%m/%d')

    