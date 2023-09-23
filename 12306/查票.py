import pandas as pd
import requests
import pprint
import prettytable as pt
import json

f = open('city.json', encoding='utf-8')
json_data = json.loads(f.read())
# print(json_data)
while True:
    from_city = input("请输入出发城市：")
    to_city = input("请输入到达城市：")
    date = input("请输入乘车时间(2022-09-18/年-月-日)：")
    s1 = json_data[from_city]
    s2 = json_data[to_city]
    print(s1, s2)

    url = f'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={s1}&leftTicketDTO.to_station={s2}&purpose_codes=ADULT'
    print(url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=%E4%B8%8A%E6%B5%B7,SHH&ts=%E5%8C%97%E4%BA%AC%E5%8C%97,VAP&date=2022-09-17&flag=N,N,Y',
        'Cookie': '_uab_collina=165710763242016039286799; JSESSIONID=1B7F5F401E2483AA0208C76FC1A069C0; _jc_save_wfdc_flag=dc; BIGipServerpassport=971505930.50215.0000; RAIL_EXPIRATION=1663642425393; RAIL_DEVICEID=UQa_WWyBnsJ-o47s5sCaspoIjseyvbOQeut1zDAYILPxD1CnUyU1T6L1g7vq8iiN1qi5VL6azQ-8wA_Ek1cV09X59itUTm8lyAe71-RF3PkpVxnLBqXhfCwkGHMY3ZJkqs_BLD7wDbn7PSKY2xXNX8daDfoDBdKo; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; _jc_save_fromDate=2022-09-17; _jc_save_toDate=2022-09-17; route=c5c62a339e7744272a54643b3be5bf64; fo=9yn67uyxi1jlqpejhoRIvklY5aSGx_RrooEwyKKu4INCVRrWQONRCzG3-Kpt5m7LmqRPFJUslOT0fIdh3gP3XKaabpVnpqrwhvB9J2eg6Cl4lvht6uectc4ZMyR-28vhTMm953x2pYiK_IjlZvAuQR_T9kj2Ba4ScTJL1UTpE_UYanqw-_Lf7DS06s8; BIGipServerpool_passport=65274378.50215.0000; _jc_save_fromStation=%u4E0A%u6D77%2CSHH; _jc_save_toStation=%u5317%u4EAC%u5317%2CVAP; BIGipServerotn=451936778.64545.0000'
    }

    response = requests.get(url, headers=headers).json()
    # print(response)
    # pprint.pprint(response)
    res = response['data']['result']
    lis = []
    tb = pt.PrettyTable()
    tb.field_names = [
        '序号',
        '车次',
        '出发时间',
        '到达时间',
        '需用时间',
        '日期',
        '特等座',
        '一等',
        '二等',
        '硬卧',
        '硬座',
        '无座',
        '软卧',
    ]
    num = 0
    # print(res)
    for index in res:
        info_list = index.split('|')
        trainNumber = info_list[3]  # 车次
        start_time = info_list[8]  # 出发时间
        end_time = info_list[9]  # 到达时间
        need_time = info_list[10]  # 需用时间
        data_time = info_list[13]  # 日期
        specialClass = info_list[32]  # 特等座
        first_class = info_list[31]  # 一等
        second_class = info_list[30]  # 二等
        hardSleeper = info_list[28]  # 硬卧
        hardSeat = info_list[29]  # 硬座
        noSeat = info_list[26]  # 无座
        softSleeper = info_list[23]  # 软卧

        # num = 0
        # for i in info_list:
        #     print(i, num, sep='-')
        #     num += 1
        # break
        dit = {
            '车次': trainNumber,
            '出发时间': start_time,
            '到达时间': end_time,
            '需用时间': need_time,
            '日期': data_time,
            '特等座': specialClass,
            '一等': first_class,
            '二等': second_class,
            '硬卧': hardSleeper,
            '硬座': hardSeat,
            '无座': noSeat,
            '软卧': softSleeper,
        }

        lis.append(dit)
        tb.add_row([
            num,
            trainNumber,
            start_time,
            end_time,
            need_time,
            data_time,
            specialClass,
            first_class,
            second_class,
            hardSleeper,
            hardSeat,
            noSeat,
            softSleeper,
        ])
        num += 1
        # print(dit)
    print(tb)
    # data = pd.DataFrame(lis)
    # print(data)
    again = input('是否继续查询(Y/N): ')
    if again == 'Y' or again == 'y':
        continue
    else:
        break

