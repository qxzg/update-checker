import requests
import re
from bs4 import BeautifulSoup

Base_Url = "https://koolshare.cn/thread-139965-1-1.html"
headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}


def get_info():
    req = requests.get(url=Base_Url, headers=headers, timeout=15)
    req.encoding = "UTF-8"
    soup = BeautifulSoup(req.text, "lxml")
    title = soup.title.string
    releasedate = str(re.findall(r"【(\d{8})】", title)[0])
    data = {
        "Version": re.findall(r"RT-AC86U_(.*) 官改固件", title)[0].replace(".", "_"),
        "ReleaseDate": '-'.join([releasedate[:4], releasedate[4:6], releasedate[6:8]])
    }
    data['ChangeLogUrl'] = "https://koolshare.cn/thread-139965-1-1.html#%s%s年%s月%s日" % (
        data['Version'].replace("_", ""), releasedate[:4], releasedate[4:6], releasedate[6:8])
    return data


def check_update(latest_version):
    data = get_info()
    latest_version = latest_version.split('_')
    ver2 = data['Version'].split('_')
    print(latest_version, ver2)
    if len(latest_version) == len(ver2):
        for i in range(len(latest_version)):
            if int(latest_version[i]) < int(ver2[i]):
                return ["success", 1, data['Version'], data['ReleaseDate'], "#### AC86U官改%s已发布  \n #### 更新日志见：%s" % (data['Version'].replace("_", "."), data['ChangeLogUrl'])]
        return ["success", 0]
    else:
        return ["success", 1, data['Version'], data['ReleaseDate'], "#### AC86U官改%s已发布  \n #### 更新日志见：%s" % (data['Version'].replace("_", "."), data['ChangeLogUrl'])]


if __name__ == "__main__":
    print(check_update("384_9318_3"))
