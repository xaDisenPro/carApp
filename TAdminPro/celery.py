from __future__ import absolute_import
import os

from celery import Celery

from TAdminPro import settings


# 设置系统环境 DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'TAdminPro.settings')

app = Celery('TAdminPro')

# 配置Celery
app.config_from_object('django.conf:settings')

# 自动从所有当前项目已安装的app中 查找 tasks 任务
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)



