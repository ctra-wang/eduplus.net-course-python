from authorization import CREDIT


def init(page_number):
    import requests

    # 请求头
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en,zh;q=0.9,zh-CN;q=0.8',
        'Connection': 'keep-alive',
        'Cookie': 'SESSION=' + CREDIT,
        'Host': 'www.eduplus.net',
        'Referer': 'https://www.eduplus.net/lab/Dataset_Index',
        'Sec-Ch-Ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Access-Token': CREDIT
    }

    # 请求地址
    url = 'https://www.eduplus.net/api/bigdata/datasets'

    # 请求参数
    params = {
        'pageNumber': page_number,
        'pageSize': 50,
        'scopeType': 'All',
        'type': 'Communal',
        'details': 'classify,at,file,by'
    }

    # 发送GET请求
    response = requests.get(url, headers=headers, params=params)

    # 打印响应内容
    print(response.text)

if __name__ == '__main__':
    # 2024-05-14日：目前共计 98 条 ，50长度分页 2页
    for i in range(1, 3):
        print(i)
        init(i)