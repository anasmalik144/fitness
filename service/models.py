from django.db import models
class servicedata(models.Model):
    ser_hed=models.CharField(max_length=60)
    ser_data=models.TextField(max_length=200)
    ser_img=models.FileField(upload_to="service/",max_length=250,null=True,default=None)
# Create your models here.
