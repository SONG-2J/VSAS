# 获取评论

# 发送请求
import requests
import pandas as pd
# 每次请求停2s，太快会被B站拦截。
import time

# 只爬个5集
oids = ['40964489', '41675896', '42378662', '42539263', '43617154']


# 爬虫类（面向对象）
class JsonProcess:
    def __init__(self):
        self.dataList = []
        self.Json_data = ''
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
        }

    # 发送爬取请求
    def spider(self, URL):
        url = URL
        response = requests.get(url, headers=self.headers, verify=False)
        response.encoding = 'utf-8'
        self.Json_data = response.json()['data']['replies']


# 爬取根评论
def getReplies(jp, i, oid):
    # 不知道具体有多少页的评论，所以使用死循环一直爬
    while i<=20:
        url = f'https://api.bilibili.com/x/v2/reply/main?jsonp=jsonp&next={i}&type=1&oid={oid}&mode=3&plat=1&_=1647577851745'
        jp.spider(url)
        # 如果当前页为空（爬到头了），跳出循环，程序结束。
        if jp.Json_data is None:
            break
        for node in jp.Json_data:
            print('===================')
            name = node['member']['uname']  # 昵称
            ctime = node['ctime']  # 发布时间戳
            sex = node['member']['sex']  # 性别
            rcount = node['rcount']  # 回复
            like = node['like']  # 点赞
            content = node['content']['message']  # 评论
            lv = node['member']['level_info']['current_level']  # 等级
            data = [name, lv, sex, ctime, rcount, like, content]
            print(data)
            # f.writelines(','.join(list(map(str, data))) + '\n')
            jp.dataList.append(data)
        # 每爬完一页，页数加1
        i += 1
        time.sleep(2)


if __name__ == '__main__':
    for i in range(len(oids)):
        fileName = 'comments/1818黄金眼-' + str(i + 1) + '.csv'
        # f = open(fileName, 'a')
        # f.writelines(','.join(['name', 'level', 'sex', 'ctime', 'rcount', 'like', 'content']) + '\n')
        JP = JsonProcess()
        getReplies(JP, 1, oids[i])
        df = pd.DataFrame(JP.dataList, columns=['name', 'level', 'sex', 'ctime', 'rcount', 'like', 'content'])
        df.to_csv(fileName, index=False)
        # f.close()
    print('\n================存储完成================\n')
