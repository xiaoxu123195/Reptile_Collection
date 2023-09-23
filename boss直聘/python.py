import requests
import re
for i in range(1, 11):
    link = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=%E5%8C%97%E4%BA%ACpython&city' \
           f'=100010000&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=&page={i}' \
           '&pageSize=30 '
    print(link)
    # data = {
    #     'scene': '1',
    #     'query': '北京python',
    #     'city': '100010000',
    #     'experience': '',
    #     'degree': '',
    #     'industry': '',
    #     'scale': '',
    #     'stage': '',
    #     'position': '',
    #     'salary': '',
    #     'multiBusinessDistrict': '',
    #     'page': '1',
    #     'pageSize': '30',
    # }

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'cookie': 'wd_guid=4939db9c-d326-402b-8a3f-82aecae209f4; historyState=state; _bl_uid=zCleh5sn2t5ehk77I9tn7d35a2a9; __fid=becfaa13ea044fdcec95a036ba52049c; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1656812749,1657004833,1657253595,1657273073; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1657273073; __g=-; __zp_stoken__=1cfddf0xuOUMifDlMXm8%2FJDwxSxQ3QldDdBUCKi5%2FIQpjdmlnJFEAc18aMl5hfVIwEwNqD2N%2BSVRLGnU8cUx7GRp4T3c%2BR0dmWGd7YDlPPRALZjlyVGlXXVASJH4XZFZlegg6RH8GQwQraBR2Ex9hIFcYRyoKFWBLFAAERzcDEhEfbTB3IhgMXlwRRzVVXWQbYA5Qb2lHRg%3D%3D; __c=1657273073; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E5%258C%2597%25E4%25BA%25ACpython%26city%3D100010000&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DHooUIDMIPl9-VZhQaPfYuiwOetp4bBF5PHyxPxjR07cKxGOzg0fLY_TnG0eUb706%26wd%3D%26eqid%3Db71f07710001aa340000000262c7faed&g=&s=3&friend_source=0&s=3&friend_source=0; __a=41916942.1655789213.1657253596.1657273073.92.15.7.92'
    }

    response_data = requests.get(url=link, headers=headers).text

    # print(response_data)




