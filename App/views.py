from random import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from App.models import *





def homeBlog(request):
    titles = Blog.objects.all()
    context = {'titles': titles}
    return render(request, 'myblog.html', context)




def homeContent(request,btitle):
    b = Blog.objects.filter(btitle=btitle)[0]
    b.bcount += 1
    b.save()
    contents = Content.objects.filter(ctitle__btitle__contains='%s'%btitle)
    context = {'contents':contents, 'btitle':btitle,'b':btitle}
    return render(request,'blogpage.html',context)


def addBlog(request):
    b = Content()
    b.btitle = '标题2'
    b.bname = '作者2'
    b.bcount =0
    b.save()
    return HttpResponse('添加成功')

def addContent(request):
    c = Content()
    g = Blog.objects.last()
    c.ctitle = g
    c.cname = '作者2'
    c.cinfo = 'MVC即模型－视图－控制器模式，就是为那些需要为同样的数据提供多个视图的应用程序而设计的。它很好地实现了数据层与表示层的分离，特别适用于开发与用户图形界面有关的应用程序。控制器用来处理用户命令以及程序事件；模型维护数据并提供数据访问方法；视图用于数据的显示。'
    c.save()
    return HttpResponse('添加成功')


#----------------------------------
def index(request):
    eassy = Eassy.objects.all()
    context = {'eassy':eassy}
    return render(request,'index.html',context)

def detail(request, title):
    eassy = Eassy.objects.filter(etitle=title)[0]
    eassy.ecount += 1
    eassy.save()
    context = {'eassy': eassy}
    return render(request, 'detail.html', context)