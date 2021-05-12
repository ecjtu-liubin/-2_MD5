from django.db import models


# Create your models here.
class loguser(models.Model):
    username = models.CharField(max_length=20,verbose_name='用户名')
    password = models.CharField(max_length=100,verbose_name='密码')
