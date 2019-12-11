import requests
import json

import base64
import datetime
import zlib
def encode_token():
    ts = int(datetime.datetime.now().timestamp() * 1000)
    token_dict = {
        'rId': 100051,
        'ts': ts,
        'cts': ts + 100 * 1000,
        'brVD': [1920, 192],
        'brR': [[1920, 1080], [1920, 1040], 24, 24],
        'bI': ["https://www.meituan.com/jiudian/1397563437/","https://qd.meituan.com/s/%E7%94%B5%E7%AB%9E%E9%85%92%E5%BA%97/"],
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


print(encode_token())