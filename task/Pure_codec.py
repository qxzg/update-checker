import requests
from bs4 import BeautifulSoup

Base_Url = "https://jm.wmzhe.com/"


def get_info():
    global request_data
    req = requests.get(url=Base_Url, timeout=15)
    req.encoding = "UTF-8"
    soup = BeautifulSoup(req.text, "lxml")
    request_data = {
        'Version': int(soup.find("span", id="version").string),
        'ReleaseDate': soup.find("span", id="utime").string.replace("/", "-"),
        'DownloadUrl': soup.find_all("a")[1].get('href')
    }
    return


def check_update(latest_version):
    get_info()
    latest_version = int(latest_version)
    if latest_version < request_data['Version']:
        return ["success", 1, request_data['Version'], request_data['ReleaseDate'], "####  完美解码V.%d 已发布  \n #### 下载地址： %s" % (request_data['Version'], request_data['DownloadUrl'])]
    else:
        return ["success", 0]


if __name__ == "__main__":
    print(check_update(20200000))
