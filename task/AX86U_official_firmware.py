import requests

Base_Url = "https://www.asus.com.cn/support/api/product.asmx/GetPDDrivers?osid=8&website=cn&pdhashedid=pezdd5ujcut73gz5&model=RT-AX86U"
headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}
asus_webpage_url = "https://www.asus.com.cn/Networking-IoT-Servers/WiFi-6/All-series/RT-AX86U/HelpDesk_BIOS/"


def get_info():
    global request_data
    req = requests.get(url=Base_Url, headers=headers, timeout=15)
    req.raise_for_status()  # 检查返回值
    req_date = req.json()
    request_data = {
        'Version': req_date['Result']['Obj'][0]['Files'][0]['Version'],
        'ReleaseDate': req_date['Result']['Obj'][0]['Files'][0]['ReleaseDate'],
        'DownloadUrl': req_date['Result']['Obj'][0]['Files'][0]['DownloadUrl']['China'],
        'Text': req_date['Result']['Obj'][0]['Files'][0]['Description'].replace("<br/><br/>", "<br/>".replace("<br/>", "  \n##### "))
    }


def check_update(latest_version, logger=None):
    get_info()
    ver1 = latest_version.split('.')
    ver2 = request_data['Version'].split('.')
    logger.debug(str(ver1) + str(ver2))
    if len(ver1) != len(ver2):
        return ["error", "[AX86U_official_firmware] 版本号长度不匹配"]
    for i in range(len(ver1)):
        if int(ver1[i]) < int(ver2[i]):
            release_date = request_data['ReleaseDate'].replace("/", "-")
            text = "请前往[%s](%s)下载  \n#### 更新日志：  \n##### " % (asus_webpage_url, asus_webpage_url)+ \
                request_data['Text']
            return ["success", 1, request_data['Version'], release_date, text]
    return ["success", 0]


if __name__ == '__main__':
    print(check_update("3.0.0.4.382.123"))
