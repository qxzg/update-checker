import requests
from bs4 import BeautifulSoup
import json

Base_Url="https://www.asus.com.cn/support/api/product.asmx/GetPDDrivers?osid=8&website=cn&pdhashedid=pezdd5ujcut73gz5&model=RT-AX86U"

def get_version():
    req = requests.get(url=Base_Url)
    req.raise_for_status() #检查返回值
    req_date = req.json()
    print(req_date['Result']['Obj'][0]['Name'])
    print(req_date['Result']['Obj'][0]['Files'][0]['Version'])
    print(req_date['Result']['Obj'][0]['Files'][0]['ReleaseDate'])
    print(req_date['Result']['Obj'][0]['Files'][0]['DownloadUrl']['China'])
    print(req_date['Result']['Obj'][0]['Files'][0]['Description'])
    return

get_version()