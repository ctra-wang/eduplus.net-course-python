from datetime import datetime

import requests
import json

from authorization import CREDIT


def init(page_number):
    # 请求头
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en,zh;q=0.9,zh-CN;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '71',
        'Content-Type': 'application/json',
        'Cookie': 'SESSION=' + CREDIT,
        'Host': 'www.eduplus.net',
        'Origin': 'https://www.eduplus.net',
        'Referer': 'https://www.eduplus.net/course/u/resourceStore/theroryCourse',
        'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Access-Token': CREDIT
    }

    # 请求参数
    # 这里pageNumber 可以从 1 一直向后取（目前看到头是7页）
    data = {
        "search": "",
        "pageNumber": page_number,
        "pageSize": 50,
        "usable": False,
        "labelMap": {}
    }

    # 请求地址
    url = 'https://www.eduplus.net/api/course/lib_courses/quality/authorized'

    # 发送POST请求
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # 打印响应内容
    print(response.text)


if __name__ == '__main__':
    # credit = "MjliNjI2ZTgtMDM5OS00YjUwLTliNGItYWQxZWNhYTk4ZGIz"
    for i in range(1, 8):
        print(i)
        init(i)
