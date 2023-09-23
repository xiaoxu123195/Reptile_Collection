import requests
import json

url = 'https://vd6.l.qq.com/proxyhttp'
headers = {
    'Host': 'vd6.l.qq.com',
    'Origin': 'https://v.qq.com',
    'Cookie': 'RK=jnikO45PM7; ptcz=e0558d2ac5536acd101b4b96b0109bdbdd65ffb0221c5cfb85c98be8af538523; tvfe_boss_uuid=7eb284fd88e097f0; pgv_pvid=4867830890; appuser=164C47CE6946A599; o_cookie=2057099774; fqm_pvqid=bc5d6967-47c9-47d5-987f-d55e5aa78fe9; pac_uid=1_2057099774; iip=0; eas_sid=W1N6i4m974Z7e1v0o9o6F6s5X5; ptui_loginuin=2057099774; lskey=00010000e2b9f19bf4a607e898d297d5ad5b0ab403051dde8a257df425b5add60de6984eb8d65010ceee0f73; pgv_info=ssid=s1280742804; lv_play_index=73; vversion_name=8.2.95; video_omgid=23ff34f47bb27805; o_minduid=hHDRrbxOu2mUE1ltzvIFwhyVWJQnKqDk; Lturn=683; LKBturn=163; LPVLturn=196; LPLFturn=692; LDERturn=676',
    'Content-Type': 'text/plain;charset=UTF-8',
    'Referer': 'https://v.qq.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}
data = '{"buid":"vinfoad","vinfoparam":"charge=0&otype=ojson&defnpayver=1&spau=1&spaudio=0&spwm=1&sphls=2&host=v.qq.com&refer=v.qq.com&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200owkcck4%2Ff0043bpxr53.html&sphttps=1&encryptVer=8.1&cKey=7CC72A34339002643037E328F5FFDEE0D0FB3D1B4E04623E68179B46D55B2A2066A880D8D45147150A669E8B45F2CF243F712B0661960DF110888290543E5CF8E8CB873242AFE250CF8EEBB8CEECF59320AB8B12EEEB0F93C2FDE56DA74F76E91247D6B0DFD244000678BE8A470F66326B1DEAD14D89685B7C0B8C4F854DB43F015C0B6F0BAD6F3972548E3F408AA1BE3C9F07190FFC7E90326A13EA5BA2C6AA91902D4C6DCEA354F649BA5600BEC18C4C2BCF4D39108BC72F43F66E27A28C748F3AEB262B1C1CC27C02E219CDF7319D70DCE60D7A193FD032CE61008FACB4A63C79A14F31BB58C32754D0158A7EF24032CC09922D1099CE71C8B6A880C9E32C&clip=4&guid=23ff34f47bb27805&flowid=c2941dfa48496069de3534b8fd37de47&platform=10201&sdtfrom=v1010&appVer=3.5.57&unid=&auth_from=&auth_ext=&vid=f0043bpxr53&defn=&fhdswitch=0&dtype=3&spsrt=2&tm=1658976229&lang_code=0&logintoken=&spvvpay=1&spadseg=3&hevclv=16&spsfrhdr=0&spvideo=0&drm=40","adparam":"pf=in&pf_ex=pc&pu=-1&pt=0&platform=10201&from=0&flowid=c2941dfa48496069de3534b8fd37de47&guid=23ff34f47bb27805&coverid=mzc00200owkcck4&vid=f0043bpxr53&chid=0&tpid=1&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fsearch%2F%3Fq%3D%25E6%259C%2588%25E7%2590%2583%25E9%2599%25A8%25E8%2590%25BD%26stag%3D2%26smartbox_ab%3D4828328&url=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fmzc00200owkcck4%2Ff0043bpxr53.html&lt=&opid=&atkn=&appid=&uid=&tkn=&rfid=e1bf831deef36600fbb5973eae45141a_1648517503&v=1.4.119&vptag=www_baidu_com%7Cx&ad_type=LD%7CKB%7CPVL&live=0&appversion=1.5.4&ty=web&adaptor=1&dtype=1&resp_type=json"}'
response = requests.post(url, headers=headers, data=data).json()
vinfo = response['vinfo']
json.loads(vinfo)
print(vinfo)


