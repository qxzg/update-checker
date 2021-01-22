import requests

Base_Url = "https://download.freenas.org/latest/CHECKSUMS.json"


def get_info():
    global request_data
    req = requests.get(url=Base_Url, timeout=15)
    req_data = req.json()
    request_data = {
        'Version': int(req_data['date']),
        'ReleaseDate': '-'.join([req_data['date'][:4], req_data['date'][4:6], req_data['date'][6:8], req_data['date'][8:10], req_data['date'][10:12]]),
        'Text': req_data['arch']['amd64'][0]['filename'][:-4]
    }


def check_update(latest_version):
    get_info()
    latest_version = int(latest_version)
    if latest_version < request_data['Version']:
        return ["success", 1, request_data['Version'], request_data['ReleaseDate'], "#### " + request_data['Text'] + " 已发布  \n #### Changelog: https://www.ixsystems.com/blog/library/" + request_data['Text'].lower().replace(".", "-")]
    else:
        return ["success", 0]


if __name__ == "__main__":
    print(check_update("202012090224"))
