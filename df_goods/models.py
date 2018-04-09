from django.db import models
from tinymce.models import HTMLField
class TypeInfo(models.Model):
    ttitle=models.CharField(max_length=20)
    isDelete=models.BooleanField(default=False)
    class Meta:
        db_table='typeinfo'
    def __str__(self):
        return self.ttitle.encode('utf-8')

class GoodsInfo(models.Model):
    gtitle=models.CharField(max_length=20)
    gpic=models.ImageField(upload_to='df_goods')
    gprice=models.DecimalField(max_digits=5,decimal_places=2)
    gunit=models.CharField(max_length=20,default='500g')
    gclick=models.IntegerField()
    gjianjie=models.CharField(max_length=200)
    gkucun=models.IntegerField()
    gdetail=HTMLField()
    isDelete=models.BooleanField(default=False)
    gtype=models.ForeignKey(TypeInfo)
    class Meta:
        db_table='goodsinfo'
    def __str__(self):
        return self.gtitle.encode('utf-8')
# Create your models here.
