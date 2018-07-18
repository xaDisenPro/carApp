from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=50, verbose_name='用户名')
    passwd = models.CharField(max_length=50, verbose_name='口令')
    email = models.CharField(max_length=50, verbose_name='邮箱')

    img = models.ImageField(verbose_name='头像',
                            upload_to='user/images')
