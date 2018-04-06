from django.db import models

class UserInfo(models.Model):
    uname=models.CharField(max_length=20)
    upassword=models.CharField(max_length=40)
    uemall=models.CharField(max_length=30)
    ushou=models.CharField(max_length=20,default='')
    uaddress=models.CharField(max_length=100,default='')
    uyoubian=models.CharField(max_length=6,default='')
    uphoto=models.CharField(max_length=11,default='')
    class Meta:
        db_table='userinfo'
# Create your models here.
