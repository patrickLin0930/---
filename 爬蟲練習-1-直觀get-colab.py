import requests as re
from bs4 import BeautifulSoup as bea

##索取網頁內容
response = re.get("https://news.baidu.com/")

##網頁內容剖析
soup=bea(response.text,'html.parser')##(.txt為指定只要res中的文字部分，html.parser為解析模式)

soup ##應該能看到解析回來的東西，這些之後要定位之後爬取

##網頁內容定位
news=soup.select('.mod-tab-content a')##參數為f12後找到的要爬取的內容所在的最上層class  ##a為指定取得a標籤的文字
##select之後的資料是用list存放，內容可能包含不要的資料
clean_news=news[0:37]##把news list中第0~36的資料移過去
clean_news ##顯示這36個資料

##網頁內容爬取
for i in clean_news :
  print(i.text)
  print(i['href'])
