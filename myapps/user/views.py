from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from user.forms import RegistForm


def regist(request):
    if request.method == 'POST':
        # 用户注册
        form = RegistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # 登录成功之后的进入登录页面
            return redirect('/user/login/')
        else:
            print(form.errors)  # html的标签
            print(form.errors.as_json())
            return render(request, 'user/regist.html',
                   {'form': form,
                    'errors': form.errors})
    else:
        # 到达 用户注册页面
        return render(request, 'user/regist.html')


def login(request):
    return HttpResponse('login')