from django.db import models

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/')
    module = models.ForeignKey('Module', on_delete=models.CASCADE)

class Module(models.Model):
    key = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    credits = models.IntegerField()

