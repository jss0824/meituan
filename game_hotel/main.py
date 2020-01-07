# -*- coding: utf-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler
import os
# from baidu_redis.keywords import get_keyword
# 将start_url 存储到redis中的redis_key中，让爬虫去爬取

def send_url():
    os.system("scrapy crawl gameHotel")

if __name__ == "__main__":
    sched = BlockingScheduler()
    sched.add_job(send_url, 'cron', month='1-12', day='1-31', hour=23, minute=10,id='game_hotel')
    sched.start()
# os.system("scrapy crawl gameHotel")
