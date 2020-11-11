import json
import requests

Base_Url="https://www.asus.com.cn/support/api/product.asmx/GetPDDrivers?osid=8&website=cn&pdhashedid=pezdd5ujcut73gz5&model=RT-AX86U"

def get_version():
    req = requests.get(url=Base_Url)
    req.raise_for_status() #检查返回值
    req_date = req.json()
    print(req_date['Result']['Obj'][1]['Name'])
    print(req_date['Result']['Obj'][1]['Files'][0]['Version'])
    print(req_date['Result']['Obj'][1]['Files'][0]['ReleaseDate'])
    print(req_date['Result']['Obj'][1]['Files'][0]['DownloadUrl']['China'])
    print(req_date['Result']['Obj'][1]['Files'][0]['Title'])
    return

# get_version()