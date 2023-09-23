import requests

url = 'https://v3-dy-o.zjcdn.com/82f45e5a84605ecb9f6abfff1c83c5bf/62d7bf2f/video/tos/cn/tos-cn-ve-15-alinc2/1355fbac68c046bc87a52ac259d6b9d6/?a=6383&ch=26&cr=0&dr=0&lr=all&cd=0%7C0%7C0%7C0&cv=1&br=941&bt=941&cs=0&ds=3&ft=bvTKJiQPRUU~fusdX672tqYlfeslfxUFWerrkXOma1k5A51&mime_type=video_mp4&qs=0&rc=ZTUzZDc4NjVpZ2hkNWRpNkBpM3NqOjY6Zmc4OzMzNGkzM0A0XjAxYS1fNWIxYTBiXzJgYSNwYDNfcjRvcGZgLS1kLTBzcw%3D%3D&l=202207201535340102100570402200C5A4'

headers = {
    'cookie': 'ttcid=2434dba2238e4cbd8fdf5cee03724ae130; ttwid=1%7Ccr1JDv1IE0jov9oNOnzgblibuCGt0AhTNI7pVy5LGIM%7C1636518215%7C630c32374596aad6fdccb0ef2b36b2bec2691722cffa5a01ddb386628edf8ca5; odin_tt=a5edbbe1e68296f878be473c96963c159a950fafcf999a959592ec015c0e00a8e56508d693817578574a391515a26f5da14e2030f31eaa31a16f4f6d3b016c5f; DOUYIN_WEB_HIDE_IM_LOGIN_GUIDE=1; AVATAR_FULL_LOGIN_GUIDE_ITA_COUNT=%224%22; AVATAR_FULL_LOGIN_GUIDE_ITA_TIMESTAMP=%221654144795746%22; s_v_web_id=verify_l4dewtc4_V6fjGMX0_arXg_4Bew_9X5z_RhsiXhHeoZ1G; home_can_add_dy_2_desktop=%220%22; _tea_utm_cache_2018=undefined; pwa_guide_count=%223%22; passport_csrf_token=47729ba7a75d6e97ad4addb21b7d435c; passport_csrf_token_default=47729ba7a75d6e97ad4addb21b7d435c; THEME_STAY_TIME=%22299516%22; IS_HIDE_THEME_CHANGE=%221%22; download_guide=%223%2F20220719%22; __ac_nonce=062d7ab490091b154815c; __ac_signature=_02B4Z6wo00f016.penwAAIDChGMhuIUETWuvzX7AAIk214qHh-C.5-xX1ixtKivxIJwUX.xpUrpk0w5iEGi3NBeCqnE3YxDNhJ7Wr7RYzHxfhH.2SkxOfrGZ4a5qUP8dOVJP-lpG1nuhCYN791; strategyABtestKey=1658301259.269; douyin.com; msToken=B1BoxZzlI0VDHVxp82RX6Im76cPlCrq-pqDu_SSNiACbSnqDy6HeD180smmhSIEI9DACgW2LdgRTZcbv3YJdkrsj7gTgaaBQtKdSomZd6Le0rXVCjDV-IVmWTeEq41qj37y05w==; tt_scid=W7qoEaj9CsmbndBj88JqjEbC1FYf75E.1ESTSNKhRkbg8pcI1AaRvuDViXvKz94Nf822; msToken=AP8JBbdOnKhVf8RcSvMAAVLwyfQh7A7hT6oL477iJlsF8NVn7SWnYT7z4xc1esVDav8dP0NtRAFLO47SmteD3jKIrs0cpUzihluE_AjgiA3JIBN1irk3eCCt-2wG1s7BhJONbQ==',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

response = requests.get(url=url, headers=headers).content
with open('video\\' + "柯基" + '.mp4', mode='wb') as f:
    f.write(response)
