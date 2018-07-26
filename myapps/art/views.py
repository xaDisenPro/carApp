import logging

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from art.models import Art
from art.tasks import readArt

from art.utils import rds

def list_art(request):
    arts = Art.objects.all()

    topArts = getArtTop(3)

    return render(request,
                  'art/list.html',
                  locals())


# n = 3
# rds.zrevrange('artTop',0,n-1, withscores=True)
# [(b'1', 15.0), (b'2', 13.0), (b'3', 8.0)]
# 返回 [(<Art> ,15), (<Art>, 13)]
def getArtTop(n):
    topn = rds.zrevrange('artTop', 0, n-1, withscores=True)
    print('-top-->', topn)

    ids = [int(id.decode()) for id,score in topn]
    print('-top ids -->', ids)

    arts = Art.objects.in_bulk(ids)
    # {1: <Art>, 2: <Art>}
    print('-top arts -->', arts)

    # 将查询对象 和 ids排序
    arts_top = [(arts.get(int(id.decode())),
                 score) for id,score in topn]

    return arts_top

def show(request, id):
    # 打印日志
    logging.getLogger('mdjango').warning('正在阅读: '+id)

    art = Art.objects.get(id=id)

    # 将当前阅读文章写入到排行中
    rds.zincrby('artTop', id, 1)  # artTop 为 key, id为member, score 默认为1

    return render(request,'art/show.html', locals())


# 抢读功能
def topReadArt(request,id):
    # 异步执行的任务
    readArt.delay(101, int(id))
    return HttpResponse('<h3>正在排队，请等等..</h3>')

def topReadArtResult(request,id):

    # 查看当前用户抢读 id 这本书的状态
    rid = rds.hget('readedArt', 101)
    if id and int(rid.decode()) == int(id):
        return JsonResponse({'code': 1,
                             'result': '已成功抢到！'})

    elif int(rid.decode()) == 0:
        return JsonResponse({'code':1,
                             'result': '已抢光！'})
    else:
        return JsonResponse({'code': 0,
                             'result': '正在抢到...'})
