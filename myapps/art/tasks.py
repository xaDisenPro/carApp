import time

from TAdminPro.celery import app
from art.utils import rds


@app.task
def readArt(uid, id):
    # 判断当前已读的数量
    reads = rds.get('readArt')
    if not reads:
        rds.set('readArt', 1)
    else:
        cnt = int(reads)
        if cnt < 5:
            rds.incrby('readArt')
            # 存储 xxx 用户 抢到 1 书的信息
            # 判断 xxx 用户是否已 抢过
            rds.hset('readedArt', uid, id)
        else:
            rds.hset('readedArt', uid, 0)
            return '已抢光'

    return '%d 用户 已抢到 %d' % (uid, id)


@app.task
def buyArt(uid, id):
    return '%d 用户 已购买 %d' % (uid, id)
