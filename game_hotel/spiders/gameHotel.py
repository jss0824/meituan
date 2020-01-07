# -*- coding: utf-8 -*-
# -*- author: Jay -*-
import scrapy
from scrapy.http import Request,FormRequest
import requests
from lxml import etree
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import datetime
import operator
import asyncio
from pyppeteer import launch
from game_hotel.items import GameHotelItem
import time
import base64
import datetime
import zlib


def stringToDate(string):
    dt =datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
    return dt


def encode_token(hotel_name):
    ts = int(datetime.datetime.now().timestamp() * 1000)
    hotel_dict = {
        '铂宿电竞酒店':'http://www.dianping.com/shop/1397563437',
        '青岛YK电竞民宿(CBD理工大学店)':'http://www.dianping.com/shop/122068331',
        '青岛YK电竞民宿(崂山大拇指广场店)':'http://www.dianping.com/shop/130749657',
        'TOP电竞酒店':'http://www.dianping.com/shop/946097146',
        'Teamwork电竞酒店':'http://www.dianping.com/shop/129009909',
        '艾克威电竞酒店':'http://www.dianping.com/shop/129151291',
        '玩家国度电竞酒店':'http://www.dianping.com/shop/130000943',
        'SOLO电竞酒店':'http://www.dianping.com/shop/130287633',
        'Online电竞酒店':'https://www.meituan.com/jiudian/1694962376',
        'Galaxy电竞民宿':'https://www.meituan.com/jiudian/513149047'
    }

    token_dict = {
        'rId': 100051,
        'ts': ts,
        'cts': ts + 100 * 1000,
        'brVD': [1920, 192],
        'brR': [[1920, 1080], [1920, 1040], 24, 24],
        'bI': [hotel_dict[hotel_name],
               "https://qd.meituan.com/s/%E7%94%B5%E7%AB%9E%E9%85%92%E5%BA%97/"],
        'mT': [],
        'kT': [],
        'aT': [],
        'tT': [],
        'sign': 'eJwlyjsOhCAUQNG9WFAafo9PQcEDSaabHRgTKShQo2Ayu5+ZeMubM+RtdQy0ooY+kWMvr98TVoMSUmhyteVsfwTWCvWg9jmyY6S3Ote8ll7dO5Dey+oSjYCamyiBYgg+SsOitCzpQJmO1gTwHEAahdJgCpNHRCFhAm8nnji583mVfZu3pWanRzHS4Qt5IiyY'
    }
    # 二进制编码

    encode = str(token_dict).encode()
    # 二进制压缩
    compress = zlib.compress(encode)
    # base64编码
    b_encode = base64.b64encode(compress)
    # 转为字符串
    token = str(b_encode, encoding='utf-8')
    return token


class GamehotelSpider(scrapy.Spider):
    name = 'gameHotel'

    def start_requests(self):
        sendToQDate_start = datetime.datetime.now().strftime('%Y-%m-%d 00:00:00')
        Date_string_start = stringToDate(sendToQDate_start)
        start = int(Date_string_start.timestamp() * 1000)

        sendToQDate_end = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')
        Date_string_end = stringToDate(sendToQDate_end)
        end = int(Date_string_end.timestamp() * 1000)


        url_list = {
                    # 铂宿
                    '铂宿电竞酒店': 'https://ihotel.meituan.com/productapi/v2/prepayList?type=1&utm_medium=PC&version_name=7.3.0&poiId=1397563437&start={}&end={}&uuid=F0D5B728D450BCCAD481D491F7C017D98C5A255486B48BFCEABBB345E5A9E2F2&_token='.format(start,end)
                    + encode_token('铂宿电竞酒店'),
                    '青岛YK电竞民宿(CBD理工大学店)': 'https://ihotel.meituan.com/productapi/v2/prepayList?type=1&utm_medium=PC&version_name=7.3.0&poiId=184555122&start={}&end={}&uuid=F0D5B728D450BCCAD481D491F7C017D98C5A255486B48BFCEABBB345E5A9E2F2&_token='.format(start,end)
                    + encode_token('青岛YK电竞民宿(CBD理工大学店)'),
                    '青岛YK电竞民宿(崂山大拇指广场店)': 'https://ihotel.meituan.com/productapi/v2/prepayList?type=1&utm_medium=PC&version_name=7.3.0&poiId=193716496&start={}&end={}&uuid=F0D5B728D450BCCAD481D491F7C017D98C5A255486B48BFCEABBB345E5A9E2F2&_token='.format(start,end)
                    + encode_token('青岛YK电竞民宿(崂山大拇指广场店)'),
                    'TOP电竞酒店': 'https://ihotel.meituan.com/productapi/v2/prepayList?type=1&utm_medium=PC&version_name=7.3.0&poiId=946097146&start={}&end={}&uuid=F0D5B728D450BCCAD481D491F7C017D98C5A255486B48BFCEABBB345E5A9E2F2&_token='.format(start,end)
                    + encode_token('TOP电竞酒店'),
                    'Teamwork电竞酒店': 'https://ihotel.meituan.com/productapi/v2/prepayList?type=1&utm_medium=PC&version_name=7.3.0&poiId=191821115&start={}&end={}&uuid=F0D5B728D450BCCAD481D491F7C017D98C5A255486B48BFCEABBB345E5A9E2F2&_token='.format(start,end)
                    + encode_token('Teamwork电竞酒店'),
                    '艾克威电竞酒店': 'https://ihotel.meituan.com/productapi/v2/prepayList?type=1&utm_medium=PC&version_name=7.3.0&poiId=191996605&start={}&end={}&uuid=F0D5B728D450BCCAD481D491F7C017D98C5A255486B48BFCEABBB345E5A9E2F2&_token='.format(start,end)
                    + encode_token('艾克威电竞酒店'),
                    '玩家国度电竞酒店': 'https://ihotel.meituan.com/productapi/v2/prepayList?type=1&utm_medium=PC&version_name=7.3.0&poiId=192911157&start={}&end={}&uuid=F0D5B728D450BCCAD481D491F7C017D98C5A255486B48BFCEABBB345E5A9E2F2&_token='.format(start,end)
                    + encode_token('玩家国度电竞酒店'),
                    'SOLO电竞酒店': 'https://ihotel.meituan.com/productapi/v2/prepayList?type=1&utm_medium=PC&version_name=7.3.0&poiId=193250283&start={}&end={}&uuid=F0D5B728D450BCCAD481D491F7C017D98C5A255486B48BFCEABBB345E5A9E2F2&_token='.format(start,end)
                    + encode_token('SOLO电竞酒店'),
                    'Online电竞酒店': 'https://ihotel.meituan.com/productapi/v2/prepayList?type=1&utm_medium=PC&version_name=7.3.0&poiId=1694962376&start={}&end={}&uuid=F0D5B728D450BCCAD481D491F7C017D98C5A255486B48BFCEABBB345E5A9E2F2&_token='.format(start,end)
                    + encode_token('Online电竞酒店'),
                    'Galaxy电竞民宿': 'https://ihotel.meituan.com/productapi/v2/prepayList?type=1&utm_medium=PC&version_name=7.3.0&poiId=513149047&start={}&end={}&uuid=F0D5B728D450BCCAD481D491F7C017D98C5A255486B48BFCEABBB345E5A9E2F2&_token='.format(start,end)
                    + encode_token('Galaxy电竞民宿'),


        }
        for url in url_list:
            headers = {
                "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            }
            yield Request(url_list[url], meta={'hotel_name':url},callback=self.parse, headers=headers, dont_filter=True)





    def parse(self, response):
        item = GameHotelItem()
        hotel_name = response.meta['hotel_name']
        print('酒店名称:',hotel_name)
        data = json.loads(response.body)
        print(data)
        for i in data['mergeList']['data']:
            print(i)
            room_type = i['roomCellName']
            print('房间类型:',room_type)
            status = i['aggregateGoods'][0]['prepayGood']['fullRoomDesc']
            if status == None:
                status = '预订'
            print('满房情况',status)

            time = {
                '1': '周一',
                '2': '周二',
                '3': '周三',
                '4': '周四',
                '5': '周五',
                '6': '周六',
                '7': '周日'
            }
            sendToQDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            apply_week = datetime.datetime.strptime(sendToQDate.split(" ")[0], "%Y-%m-%d").weekday() + 1
            weekday = time['{}'.format(apply_week)]
            Time = sendToQDate + ' ' + weekday
            print(Time)

            item['hotel_name'] = hotel_name
            item['Time'] = Time
            item['room_type'] = room_type
            item['status'] = status


            yield item




    # def __init__(self):
    #     self.browser = webdriver.Chrome()
    #     self.wait = WebDriverWait(self.browser, 20)
    #
    # def start_requests(self):
    #     url_list = [
    #                 'http://www.dianping.com/shop/1397563437',  # 铂宿
    #                 'http://www.dianping.com/shop/122068331',  # 青岛YK电竞民宿(CBD理工大学店)
    #                 'http://www.dianping.com/shop/130749657',  # 青岛YK电竞民宿(崂山大拇指广场店)
    #                 'http://www.dianping.com/shop/946097146',  # TOP电竞酒店
    #                 'http://www.dianping.com/shop/129009909',  # Teamwork电竞酒店
    #                 'http://www.dianping.com/shop/129151291',  # 艾克威电竞酒店
    #                 'http://www.dianping.com/shop/130000943',  # 玩家国度电竞酒店
    #                 'http://www.dianping.com/shop/130287633',  # SOLO电竞酒店
    #                 'http://www.dianping.com/shop/111805412'  # 铂悦电竞酒店(吾悦广场店)
    #               ]
    #     for url in url_list:
    #         headers = {
    #             "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    #             "referer": url
    #         }
    #         yield Request(url, meta={'dont_redirect': True}, callback=self.parse, headers=headers, dont_filter=True)
    #
    #
    #
    #
    #
    # def parse(self, response):
    #     item = GameHotelItem()
    #
    #
    #     # async def main():
    #     #     browser = await launch(devtools=True)
    #     #     page = await browser.newPage()
    #     #     await page.goto(url)
    #     #
    #     #     selector = etree.HTML(await page.content())
    #     #     print('html:', selector)
    #     opt = webdriver.ChromeOptions()
    #     # opt.set_headless()
    #     opt.add_experimental_option('excludeSwitches', ['enable-automation'])
    #     driver = webdriver.Chrome(options=opt)
    #     driver.get(response.url)
    #     # button = driver.find_element_by_id('yodaBoxWrapper')
    #     # action = ActionChains(driver)
    #     # action.click_and_hold(button).perform()
    #     # action.reset_actions()
    #     # action.move_by_offset(180, 0).perform()
    #     # slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'boxStatic')))
    #     # distance = 10
    #     # # 移动轨迹
    #     # track = []
    #     # # 当前位移
    #     # current = 0
    #     # # 减速阈值
    #     # mid = distance * 4 / 5
    #     # # 计算间隔
    #     # t = 0.2
    #     # # 初速度
    #     # v = 0
    #     #
    #     # while current < distance:
    #     #     if current < mid:
    #     #         # 加速度为正2
    #     #         a = 2
    #     #     else:
    #     #         # 加速度为负3
    #     #         a = -3
    #     #     # 初速度v0
    #     #     v0 = v
    #     #     # 当前速度v = v0 + at
    #     #     v = v0 + a * t
    #     #     # 移动距离x = v0t + 1/2 * a * t^2
    #     #     move = v0 * t + 1 / 2 * a * t * t
    #     #     # 当前位移
    #     #     current += move
    #     #     # 加入轨迹
    #     #     track.append(round(move))
    #     # ActionChains(self.browser).click_and_hold(slider).perform()
    #     # for x in track:
    #     #     ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
    #     # import time
    #     # time.sleep(0.5)
    #     # ActionChains(self.browser).release().perform()
    #     # driver = webdriver.Firefox()
    #
    #     data = driver.page_source
    #     # print(data)
    #     driver.close()
    #     selector = etree.HTML(data)
    #     hotel_info = selector.xpath('//*[@id="deal"]/div[1]/div[3]/div[4]/ul/li')
    #     hotel_name = selector.xpath('//*[@id="poi-detail"]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div/h1/text()')
    #     print('酒店名称：', hotel_name)
    #     room_type = []
    #     for i in hotel_info:
    #         room_type.append(('').join(i.xpath('./div[1]/div[2]/h3/text()')))
    #     print('酒店类型：', room_type)
    #
    #
    #     # soup = BeautifulSoup(data, 'lxml')
    #     soup = BeautifulSoup(data, 'lxml')
    #     room_type_list = soup.find_all(class_='title')
    #     room_type = []
    #     for i in room_type_list:
    #         for k in i.find_all(name='h3'):
    #             room_type.append(k.string)
    #     print('房间类型：',room_type)
    #
    #
    #     # hotel_info = selector.xpath('//*[@id="deal"]/div[1]/div[3]/div[4]/ul/li')
    #     status_list_first = []
    #     status_list_second = []
    #     for i in hotel_info:
    #         status_list_second.append(('').join(i.xpath('./div[3]/div[2]/div[6]/div/button/text()')))
    #         status_list_first.append(('').join(i.xpath('./div[3]/div[1]/div[6]/div/button/text()')))
    #     for i,v in enumerate(status_list_second):
    #         if len(v) != 0:
    #             for j in status_list_first:
    #                 if v != j:
    #                     status_list_first[i] = v
    #
    #     status = status_list_first
    #     print('最终：',status)
    #
    #     time = {
    #         '1': '周一',
    #         '2': '周二',
    #         '3': '周三',
    #         '4': '周四',
    #         '5': '周五',
    #         '6': '周六',
    #         '7': '周日'
    #     }
    #     sendToQDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     apply_week = datetime.datetime.strptime(sendToQDate.split(" ")[0], "%Y-%m-%d").weekday() + 1
    #     weekday = time['{}'.format(apply_week)]
    #     Time = sendToQDate + ' ' + weekday
    #     print(Time)
    #
    #     for i,j in zip(room_type, status):
    #         item['hotel_name'] = hotel_name
    #         item['Time'] = Time
    #         item['room_type'] = i
    #         item['status'] = j
    # #     await browser.close()
    # # asyncio.get_event_loop().run_until_complete(main())
    #
    #         yield item








        # url_list = ['https://www.meituan.com/jiudian/1397563437/#/616248834',   #铂宿
        #             'https://www.meituan.com/jiudian/191821115/',                #Teamwork电竞酒店
        #             'https://www.meituan.com/jiudian/184555122/',               #青岛YK电竞民宿(CBD理工大学店)
        #             'https://www.meituan.com/jiudian/193716496/',               #青岛YK电竞民宿(崂山大拇指广场店)
        #             'https://www.meituan.com/jiudian/946097146/',               #TOP电竞酒店
        #             'https://www.meituan.com/jiudian/191996605/',              #艾克威电竞酒店
        #             'https://www.meituan.com/jiudian/192911157/',               #玩家国度电竞酒店
        #             'https://www.meituan.com/jiudian/1793983031/',              #青岛天敏电竞酒店
        #             'https://www.meituan.com/jiudian/179114681/',               #铂悦电竞酒店(吾悦广场店)
        #             'https://www.meituan.com/jiudian/193250283/',               #SOLO电竞酒店
        #             ]

        # for url in url_list:
        #     opt = webdriver.ChromeOptions()
        #     opt.set_headless()
        #     driver = webdriver.Chrome(options=opt)
        #     driver.get(url)
        #
        #     data = driver.page_source
        #     driver.close()
        #     # selector = etree.HTML(data)
        #     # hotel_name = selector.xpath('//*[@id="poiDetail"]/div/div/div[2]/div/div[1]/div[1]/span/text()')
        #     # print('酒店名称：', hotel_name)
        #     soup = BeautifulSoup(data, 'lxml')
        #     hotel_name = soup.find(class_='fs26 fc3 pull-left bold').get_text()
        #     print('酒店名称：', hotel_name)
        #     status = []      #总预订状态
        #     room_type_list = soup.find_all(class_="fs18 fc3 mb15 deal-cellname")
        #     room_type = []
        #     for i in room_type_list:
        #         room_type.append(i.string)
        #     print(room_type)
        #     status_list_empty = soup.find_all(class_="W100 deal-btn")
        #     for j in status_list_empty:
        #         status_empty = j.string
        #         status.append(status_empty)
        #     status_list_full = soup.find_all(class_="W100 deal-btn-disabled")
        #     for k in status_list_full:
        #         status_full = k.string
        #         status.append(status_full)
        #     print(status)
        #     price = []
        #     price_list = soup.find_all(class_="price-number price-number-above")
        #     for i in price_list:
        #         price.append(i.string)
        #     print('价格：', price)
        #
        #     time = {
        #         '1': '周一',
        #         '2': '周二',
        #         '3': '周三',
        #         '4': '周四',
        #         '5': '周五',
        #         '6': '周六',
        #         '7': '周日'
        #     }
        #     sendToQDate = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #     apply_week = datetime.datetime.strptime(sendToQDate.split(" ")[0], "%Y-%m-%d").weekday() + 1
        #     weekday = time['{}'.format(apply_week)]
        #     Time = sendToQDate + ' ' + weekday
        #     print(Time)
        #
        #     for i,j,k in zip(room_type, status, price):
        #         item['hotel_name'] = hotel_name
        #         item['Time'] = Time
        #         item['room_type'] = i
        #         item['status'] = j
        #         item['price'] = k
        #         yield item

