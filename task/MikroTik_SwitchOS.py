import re
import time
from traceback import format_exc

import requests
from bs4 import BeautifulSoup

Base_Url = "https://mikrotik.com/download"
headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"}


def get_info():
    global request_data
    req = requests.get(url=Base_Url, headers=headers, timeout=15)
    req.encoding = "UTF-8"
    soup = BeautifulSoup(req.text, 'lxml')
    request_data = {
        'Version': str(re.findall(r'css309-(.*)\.bin', (str(soup.find_all('table', class_='table downloadTable')[2].find_all('a', href=re.compile('css309'))[0])))[0]),
        'ReleaseDate': time.strftime("%Y-%m-%d", time.localtime())
    }
    return


def check_update(latest_version, logger=None):
    try:
        get_info()
    except:
        return ["error", format_exc()]
    if latest_version != request_data['Version']:
        return ["success", 1, request_data['Version'], request_data['ReleaseDate'], "#### MikroTik SwitchOS已检测到更新  最新版本：%s  \n#### 请前往 %s 下载" % (request_data['Version'], Base_Url)]
    else:
        return ["success", 0]


if __name__ == "__main__":
    print(check_update('2.1'))
