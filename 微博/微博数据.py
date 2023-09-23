import requests
import pprint
import time
import openpyxl

workbook = openpyxl.Workbook()
sheet = workbook.active

# 1 - 10
#
# 循环爬取 10 页留言
for i in range(1, 10):
    url = 'https://m.weibo.cn/api/container/getIndex?containerid=2304131768167034_-_WEIBO_SECOND_PROFILE_WEIBO&type=uid&value=1768167034&page_type=03&page=' + str(
        i)
    print(url)
    response = requests.get(url)

    data = response.json()
    # pprint.pprint(data)
    cards = data['data']['cards']
    # 一页遍历10条
    for card in cards:
        mblog = card.get('mblog', None)
        if mblog:
            # 有内容再进行提取
            mid = mblog.get('mid', None)  # 是评论的 id  id card
            text = mblog.get('text', None)
            source = mblog.get('source', None)
            author_name = mblog.get('user', {}).get('screen_name', None)
            print([author_name, source, mid, text])
            sheet.append([author_name, source, mid, text])
            # 请求评论下面的评论
            # https://m.weibo.cn/comments/hotflow?id=4612810086816009&mid=4612810086816009&max_id_type=0
            # 爬取每一条数据下面的评论
            comments_url = 'https://m.weibo.cn/comments/hotflow?id=' + mid + '&mid=' + mid + '&max_id_type=0'
            comments_response = requests.get(comments_url)
            comments_data = comments_response.json()
            # print('comments_data', comments_data)
            data_list = comments_data.get('data', {}).get('data')
            # print('data_list', data_list)
            for comment in data_list:
                # print(comment)
                comment_text = comment['text']
                comment_mid = comment['mid']
                username = comment['user']['screen_name']
                print([username, comment_mid, comment_text])
                # 请求一条数据进行演示 jquery+layui
                # 要不要把主评论与子评论分开保存
                # 一起保存 分开保存 不晓得
                sheet.append([username, comment_mid, comment_text])
            # break
    time.sleep(2)
    # break
workbook.save('微博数据.xlsx')
