from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from user.models import UserProfile


def log_exec(func):
    def wrapper(request, *args, **kwargs):
        print('---log----', func, request.path, datetime.now())

        if request.path == '/user/login/':
            print(args, kwargs)
            allUser = UserProfile.objects.all()
            request.datas = allUser
            resp:HttpResponse = func(request,*args,**kwargs)
        else:
            resp = func(request, *args, **kwargs)
        print('end----log')
        return resp
    return wrapper