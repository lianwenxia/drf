from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True, verbose_name='手机号码')
    fixtel = models.CharField(max_length=11, unique=True, verbose_name='固定电话', null=True)
    qq = models.CharField(max_length=11, unique=True, verbose_name='qq', null=True)
    birth = models.DateField(verbose_name='出生日期', null=True)
    faceimg = models.ImageField(verbose_name='头像')

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Area(models.Model):
    '''省市区表'''
    name = models.CharField(max_length=15, verbose_name='名字')
    pid = models.ForeignKey('self', blank=True, null=True, verbose_name='所属省市区')


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', verbose_name='所属用户')
    province = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='pro', verbose_name='省')
    city = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='city', verbose_name='市')
    block = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='block', verbose_name='区')
    receive = models.CharField(max_length=20, verbose_name='收货人')
    place = models.CharField(max_length=50, verbose_name='地址')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    fixtel = models.CharField(max_length=11, verbose_name='固定电话')
    zipcode = models.CharField(max_length=10, verbose_name='邮编')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    class Meta:
        db_table = 'address'
        verbose_name = 'prov'
        verbose_name_plural = verbose_name


