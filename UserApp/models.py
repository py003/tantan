from django.db import models

# Create your models here.
class User(models.Model):
    phonenum=models.CharField(max_length=16,null=False,unique=True)
    nickname=models.CharField(max_length=32)
    gender=models.BooleanField(default=True)
    birthday=models.DateField(default='2000-01-01')
    avatar=models.ImageField(upload_to='icons')
    location=models.CharField(max_length=32)

    class Meta:
        db_table='user'