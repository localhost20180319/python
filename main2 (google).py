from bs4 import BeautifulSoup
import requests
import json


#維基百科的API路徑
url2="https://zh.wikipedia.org/w/api.php?action=opensearch&search=python"

#維基百科本身網址
#url="https://zh.wikipedia.org/wiki/Python"

#DDD=瀏覽器定義
DDD = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/115.0 Safari/537.36"
           }
# headers為get裡面原本的函式參數名稱，然後要=我設定的瀏覽器參數內容(走url的時候用)
#response = requests.get(url,headers=DDD)
#soup = BeautifulSoup(response.text, "html.parser")
#intro_paragrph = soup.select("div#mw-content-text p")[0].text
#print("第一段介紹：")
#print(intro_paragrph)

#print("\n小標題：")
#headings = soup.find_all(["h2","h3"])
#for h in headings:
#    print(h.text.strip())


#直接拿API的JSON解析(走url2專用)
response = requests.get(url2, headers=DDD)
data=json.loads(response.text)#先把url2的資料存成變數，在解析，目的是未來可以重複使用
print("確認狀態碼：",response.status_code)# 確認狀態碼
print("印出主體JSON：",response.text)#印出主體JSON
print("data變數抓過來的，變成資料list：",data)#把data變數解析JSON，變成資料list


#解析JSON(此種方法不需要特別設定變數，直接把API的JSON檔案解析出來)
print(response.json())



#print(response.status_code)
#print(response.text[:500])

#print(soup.title)
#print(soup.title.text)


