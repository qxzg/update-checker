import requests

Base_Url = "https://www.asus.com.cn/support/api/product.asmx/GetPDDrivers?osid=8&website=cn&pdhashedid=pezdd5ujcut73gz5&model=RT-AX86U"


def get_info():
    global request_data
    req = requests.get(url=Base_Url, timeout = 15)
    req.raise_for_status()  # 检查返回值
    req_date = req.json()
    request_data = {
        'Version': req_date['Result']['Obj'][1]['Files'][0]['Version'],
        'ReleaseDate': req_date['Result']['Obj'][1]['Files'][0]['ReleaseDate'],
        'DownloadUrl': req_date['Result']['Obj'][1]['Files'][0]['DownloadUrl']['China'],
        'Text': req_date['Result']['Obj'][1]['Files'][0]['Title']
    }
    """
    print(req_date['Result']['Obj'][1]['Name'])
    print(req_date['Result']['Obj'][1]['Files'][0]['Version'])
    print(req_date['Result']['Obj'][1]['Files'][0]['ReleaseDate'])
    print(req_date['Result']['Obj'][1]['Files'][0]['DownloadUrl']['China'])
    print(req_date['Result']['Obj'][1]['Files'][0]['Title'])
    """
    return


def check_update(latest_version):
    get_info()
    ver1 = latest_version.split('.')
    ver2 = request_data['Version'].split('.')
    print(ver1, ver2)
    if len(ver1) != len(ver2):
        return ["error", "[AX86U_official_sourcecode] 版本号长度不匹配"]
    for i in range(len(ver1)):
        if int(ver1[i]) < int(ver2[i]):
            release_date = request_data['ReleaseDate'].replace("/", "-")
            text = "#### " + \
                request_data['Text'] + \
                "   \n#### 请前往[华硕官网](https://www.asus.com.cn/Networking/RT-AX86U/HelpDesk_Download/)下载"
            return ["success", 1, request_data['Version'], release_date, text]
    return ["success", 0]


if __name__ == '__main__':
    print(check_update("3.0.0.4.386.41535"))
# get_version()
