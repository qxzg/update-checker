import re

import requests
from bs4 import BeautifulSoup

Base_Url = "https://koolshare.cn/thread-191637-1-1.html"
headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}


def get_info() -> dict:
    req = requests.get(url=Base_Url, headers=headers, timeout=15)
    req.encoding = "UTF-8"
    soup = BeautifulSoup(req.text, "lxml")
    title = soup.title.string
    release_date = str(re.findall(r"【(\d{8})】", title)[0])
    data = {
        "Version": re.findall(r"RT-AX86U_(.*) ML改版固件", title)[0].replace(".", "_"),
        "ReleaseDate": '-'.join([release_date[:4], release_date[4:6], release_date[6:8]])
        }
    data['ChangeLogUrl'] = "https://koolshare.cn/thread-191637-1-1.html#%s%s年%s月%s日" % (
        data['Version'].replace("_", ""), release_date[:4], release_date[4:6], release_date[6:8])
    return data


def check_update(latest_version, logger=None):
    data = get_info()
    latest_version = latest_version.split('_')
    ver2 = data['Version'].split('_')
    logger.debug(str(latest_version) + str(ver2))
    if len(latest_version) == len(ver2):
        for i in range(len(latest_version)):
            if int(latest_version[i]) < int(ver2[i]):
                return ["success", 1, data['Version'], data['ReleaseDate'],
                        "#### AX6U ML改版固件%s已发布  \n #### 更新日志见：%s" % (data['Version'].replace("_", "."), data['ChangeLogUrl'])]
        return ["success", 0]
    else:
        return ["success", 1, data['Version'], data['ReleaseDate'],
                "#### AX86U ML改版固件%s已发布  \n #### 更新日志见：%s" % (data['Version'].replace("_", "."), data['ChangeLogUrl'])]


if __name__ == "__main__":
    import logging

    print(check_update("386.1_2", logging.getLogger()))
