##這邊說明下，這邊從關卡3的程式開始延伸

from bs4 import BeautifulSoup
import requests
import json

# endpoint（不要在 url 字串裡加 也沒關係，requests 會自動組 query string），
endpoint = "https://zh.wikipedia.org/w/api.php"


#DDD=瀏覽器定義
DDD = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0 Safari/537.36"
           }


#我要的關鍵字列表
keywords = ["赴山海", "弓道", "潛水"]




#網址相關變數(關卡3)，把limit設定成變數，以及把URL相關的response、data、titles.....等等拉到def函式裡面
def my_search(keyword,limit=5):
    parms={
      "action":"opensearch",
      "search":keyword,
      "limit":limit,
      "format":"json"
          }

# 正確呼叫：第一個參數是 URL，關鍵字參數要寫 params= 和 headers=
    response = requests.get(endpoint, params=parms, headers=DDD)
    data=json.loads(response.text)#先把url2的資料存成變數，在解析，目的是未來可以重複使用

# 取標題與連結，並漂亮印出（關卡 1）
    titles=data[1]
    links=data[3]


    data=json.loads(response.text)#先把url2的資料存成變數，在解析，目的是未來可以重複使用
    print("確認狀態碼：", response.status_code)  # 確認狀態碼
    print("印出主體JSON：",response.text)#印出主體JSON
    print("data變數抓過來的，變成資料list：",data)#把data變數解析JSON，變成資料list



#配對上面data把「標題」配對「連結」並漂亮印出
    print("把「標題」配對「連結」並漂亮印出：")
    for i ,(t,l)  in enumerate(zip(titles,links),start=1):
        print(f"{i}) {t} → {l}")

for kw in keywords:
    my_search(kw)


