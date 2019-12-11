# -*- coding: utf-8 -*-
import json
from mitmproxy import ctx
def response(flow):
    # url = 'https://cars.app.autohome.com.cn'
    # cars = []
    # if 'cars' in flow.request.url:
    #     text = flow.response.text
    #     data = json.loads(text)
    #
    #     cars_info = data['result'].get('fctlist')
    #     # print('总信息',cars_info)
    #     for item in cars_info:
    #         cars_info2 = item['serieslist']
    #     # print('副信息:',cars_info2)
    #     for i in cars_info2:
    #         cars.append(i['name'])
    #     print('车辆型号：',cars)
    # else:
    #     print('无')
    print('连接：',flow.request.url)
    print('内容：',flow.response.content)