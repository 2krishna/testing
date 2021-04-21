from django.db import models

# Create your models here.
class TestingEmails(models.Model):
    files = models.FileField(upload_to='documents',null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
