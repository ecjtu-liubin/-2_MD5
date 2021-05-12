from django.shortcuts import render
from . import models
import hashlib
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        hash = hashlib.md5()
        hash.update(bytes(pwd, encoding='utf-8'))
        pwd = hash.hexdigest()
        user = models.loguser.objects.filter(username=username,password=pwd)
        if user:
            return render(request,'success.html')
        else:
            errormsg = '用户名或密码错误！'
            return render(request, 'login.html', {'error': errormsg})
    return render(request, 'login.html')


def registe(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        hash = hashlib.md5()
        hash.update(bytes(password, encoding='utf-8'))
        pwd = hash.hexdigest()
        user_obj = models.loguser.objects.create(username=username,password=pwd)
        if user_obj:
            return render(request,'success2.html')
        else:
            errormsg = "输入有误，注册失败！"
            return render(request,'registe.html',{"errormsg":errormsg})

    return render(request,'registe.html')