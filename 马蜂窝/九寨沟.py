import requests
import json
import pprint


headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Referer": "http://www.mafengwo.cn/poi/youji-5423057.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
cookies = {
    "mfw_uuid": "62a58182-69aa-55ae-dc13-3637378be74a",
    "uva": "s%3A92%3A%22a%3A3%3A%7Bs%3A2%3A%22lt%22%3Bi%3A1655013764%3Bs%3A10%3A%22last_refer%22%3Bs%3A24%3A%22https%3A%2F%2Fwww.mafengwo.cn%2F%22%3Bs%3A5%3A%22rhost%22%3BN%3B%7D%22%3B",
    "__mfwurd": "a%3A3%3A%7Bs%3A6%3A%22f_time%22%3Bi%3A1655013764%3Bs%3A9%3A%22f_rdomain%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A6%3A%22f_host%22%3Bs%3A3%3A%22www%22%3B%7D",
    "__mfwuuid": "62a58182-69aa-55ae-dc13-3637378be74a",
    "__jsluid_h": "0d3880f569ee3844215073a68e18f761",
    "_r": "baidu",
    "_rp": "a%3A2%3A%7Bs%3A1%3A%22p%22%3Bs%3A18%3A%22www.baidu.com%2Flink%22%3Bs%3A1%3A%22t%22%3Bi%3A1655697706%3B%7D",
    "__mfwc": "direct",
    "oad_n": "a%3A3%3A%7Bs%3A3%3A%22oid%22%3Bi%3A1029%3Bs%3A2%3A%22dm%22%3Bs%3A15%3A%22www.mafengwo.cn%22%3Bs%3A2%3A%22ft%22%3Bs%3A19%3A%222022-08-01+21%3A59%3A58%22%3B%7D",
    "__omc_chl": "",
    "__omc_r": "",
    "__jsl_clearance": "1659954847.616|0|ixHb%2FL2F3KZIkhPFyUg%2Btj5Ge70%3D",
    "PHPSESSID": "rq72h9cl34n91nao3j9jh2qe06",
    "__mfwb": "766eebc87ed3.1.direct",
    "__mfwa": "1655013764499.76588.12.1659519639358.1659954850734",
    "__mfwlv": "1659954850",
    "__mfwvn": "10",
    "__mfwlt": "1659954850",
    "Hm_lvt_8288b2ed37e5bc9b4c9f7008798d2de0": "1659362399,1659519640,1659520406,1659954851",
    "Hm_lpvt_8288b2ed37e5bc9b4c9f7008798d2de0": "1659954851",
    "bottom_ad_status": "0"
}
url = "http://www.mafengwo.cn/gonglve/ajax.php"
params = {
    "act": "get_new_travellist",
    "page": "2",
    "poi_id": "5423057",
    "_ts": "1659954861454",
    "_sn": "8817f0ae3a"
}
response = requests.get(url, headers=headers, cookies=cookies, params=params, verify=False)
json_data = json.loads(response.text)
print(json_data)
pprint.pprint(json_data)
