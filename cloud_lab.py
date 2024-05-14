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
        'Content-Length': '216',
        'Content-Type': 'application/json',
        'Cookie': 'SESSION=' + CREDIT,
        'Host': 'www.eduplus.net',
        'Origin': 'https://www.eduplus.net',
        'Referer': 'https://www.eduplus.net/course/u/resourceStore/experimentLibrary',
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
    data = {
        "pageNumber": page_number,
        "pageSize": 40,
        "search": "",
        "platform": "",
        "scopeType": "Public",
        "sort": "authorize",
        "order": "DESC",
        "details": ["classify", "by", "resource", "blueprint", "experimentUser", "resourcePool", "label"],
        "labelMap": {}
    }

    # 请求地址
    url = 'https://www.eduplus.net/api/bigdata/laboratories/list'

    # 发送POST请求
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # 打印响应内容
    print(response.text)


if __name__ == '__main__':
    # 2024-05-14日：目前共计 1847 条 ，40长度分也 47页
    for i in range(1, 48):
        print(i)
        init(i)
