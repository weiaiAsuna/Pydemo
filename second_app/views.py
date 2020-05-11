import math

from django.core.paginator import Paginator
from django.forms import forms
from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import render, HttpResponse, redirect

from second_app import models


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, "second/register.html")
    if request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("password")
        file = request.FILES.get("images")
        if u and p and file:
            result = models.UserInfo.objects.all()
            for i in result:
                print(u, i.username, "----")
                if u == i.username:
                    return HttpResponse("注册失败，账号已存在！")
            else:
                print("注册完成！")
                files = models.UserInfo(username=u, password=p, img=file)
                files.save()
                # return HttpResponse("ok")
                return HttpResponseRedirect('/second/login/')
        else:
            return HttpResponse("注册失败，信息没有填写！")


def login(request):
    title = "login"
    if request.method == "GET":
        return render(request, "second/login.html", {"title": title})
    if request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("password")
        if u and p:
            result = models.UserInfo.objects.all()
            for i in result:
                # print(u,p,i.username,i.password)
                if u == i.username and p == i.password:
                    request.session['login'] = '已经登录'
                    return HttpResponse("ok")

                    # return render(request, "second/index.html", {"username": u, 'welcome': "欢迎你"})
            else:
                return HttpResponse("用户名或者密码错误！")
        else:
            return HttpResponse("请输入用户名密码！")

# def pages(data,limit,page):
#     totalCount=len(data)
#     pagesize=limit
#     totalPage=math.ceil(totalCount/pagesize)
#     data_page=data[(page-1)*limit:limit*page]
#     data_dict=[d for d in data_page]
#     return totalPage,data_dict

def list(request,page):
    user_list = models.UserInfo.objects.all()
    list1=[]
    for i in user_list:
        list1.append(i)
    paginator=Paginator(list1,3)
    data=paginator.page(page)
    return render(request, "second/list.html", {"data": data,"welcome": "欢迎你"})


def download_file(request,nid):
    file=models.UserInfo.objects.filter(id=nid).first()
    filename=str(file.img).split("/")[-1]
    # 第一种方法   迭代器，对文件进行分片传输
    # response = StreamingHttpResponse(readFile(str(file.img)))
    # response['Content-Type'] = 'application/octet-stream'
    # response['Content-Disposition'] = 'attachment;filename="%s"'%filename
    # return response

    # 第二种方法
    try:
        file = open(str(file.img), 'rb')
        response = HttpResponse(file)
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        print("已经下载到默认浏览器的下载路径里！文件名是原文件名！")
        return response
    except Exception as f:
        print(f)


def readFile(filename, chunk_size=512):
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break

def json(request):
    mydata = {
        "name": "小军",
        "age": 18
    }
    # return JsonResponse(mydata)
    import json
    return HttpResponse(json.dumps(mydata), content_type="application/json")


def getjson(request):
    import json
    print(json.loads(request.body.decode("utf-8"))["params"]["ID"])
    return render(request, 'login.html')
    # pass


def user_edit(request, uid):
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=uid).first()
        return render(request, "second/user_edit.html", {"obj": obj})
    elif request.method == "POST":
        nid = request.POST.get("id")
        u = request.POST.get("username")
        p = request.POST.get("password")
        file = request.FILES.get("images")
        models.UserInfo.objects.filter(id=nid).update(username=u, password=p, names=file)
        return redirect("/second/list")


def user_del(request, nid):
    if request.method == "GET":
        models.UserInfo.objects.filter(id=nid).delete()
        return redirect("/second/list/")
