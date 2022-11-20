# 获取弹幕
import os

import requests
import re
import time
import pandas as pd

# 1818黄金眼1-14集的弹幕cid
cids = ['71955616', '73179606', '74372950', '74637778', '76427408', '77694375', '78852875', '80021850', '81199401',
        '82367334', '83627714', '84740428', '85991887', '87416016']

headers = {
    "cookie": "buvid3=0DFEE112-51F6-F856-76B1-FB921343F2E495271infoc; _uuid=D8AC11EE-1D17-81065-DCED-D7DE5553873894300infoc; buvid_fp=0DFEE112-51F6-F856-76B1-FB921343F2E495271infoc; CURRENT_FNVAL=2000; blackside_state=1; rpdid=|(k|~umkuRR)0J'uYJ))lkm~m; PVID=1; b_lsid=D4C984EF_17D947274C1; sid=aox54cdj",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}

if __name__ == '__main__':
    barrageDir = "./barrages/"
    fileName = "1818黄金眼弹幕_1-14.csv"
    barrage_list = []
    for i in range(len(cids)):
        url = "https://comment.bilibili.com/" + cids[i] + ".xml"
        page = requests.get(url=url, headers=headers)
        page.encoding = page.apparent_encoding
        tmpList = re.findall('<d p=".*?">(.*?)</d>', page.text)
        print(tmpList, '\n')
        barrage_list.append(tmpList[:])  # 添加进二维列表
        time.sleep(2)  # 太快了不好

    if not os.path.exists(barrageDir):
        os.mkdir(barrageDir)

    df = pd.DataFrame()

    for i in range(len(barrage_list)):
        df = pd.concat([df, pd.DataFrame(barrage_list[i])], axis=1)

    df.to_csv(barrageDir + fileName, index=False)
