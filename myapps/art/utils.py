from redis import Redis

from TAdminPro.settings import REDIS


rds = Redis(**REDIS)

