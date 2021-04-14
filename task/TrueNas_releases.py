from traceback import format_exc

import requests

Base_Url = "https://download.freenas.org/latest/CHECKSUMS.json"
headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"}


def get_info(proxy=None):
    global request_data
    try:
        req = requests.get(url=Base_Url, headers=headers, timeout=15)
    except:
        req = requests.get(url=Base_Url, headers=headers, timeout=15, proxies=proxy)
    req_data = req.json()
    request_data = {
        'Version': int(req_data['date']),
        'ReleaseDate': '-'.join([req_data['date'][:4], req_data['date'][4:6], req_data['date'][6:8], req_data['date'][8:10], req_data['date'][10:12]]),
        'Text': req_data['arch']['amd64'][0]['filename'][:-4]
        }


def check_update(latest_version, proxy=None, logger=None):
    try:
        get_info(proxy)
    except:
        return ["error", format_exc()]
    latest_version = int(latest_version)
    if latest_version < request_data['Version']:
        return ["success", 1, request_data['Version'], request_data['ReleaseDate'], "#### " + request_data['Text'] + " 已发布  \n #### Changelog: https://www.truenas.com/docs/releasenotes/core/" + request_data['Text'].lower().replace("-", "")[7:]]
    else:
        return ["success", 0]


if __name__ == "__main__":
    print(check_update("202012090224"))
