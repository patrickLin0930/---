import requests as re
from bs4 import BeautifulSoup as bea

##索取網頁內容

##用post的話，條件要用json或是dict來打包 這個form data是在payload找到的
form_data = {
  'SearchType': 'S',
  'Lang': 'TW',
  'StartStation': 'ZuoYing',
  'EndStation': 'BanQiao',
  'OutWardSearchDate': '2024/05/26',
  'OutWardSearchTime': '15:30',
  'ReturnSearchDate': '2024/05/26',
  'ReturnSearchTime': '15:30',
  'DiscountType': '68d9fc7b-7330-44c2-962a-74bc47d2ee8a'
}

response = re.post("https://www.thsrc.com.tw/ArticleContent/a3b630bb-1066-4352-a1ef-58c7b4e8ef7c?search=f03JL80+mmAuu/IkmM0KUfOVuVgoIcBklIxs89NGvo1Et/ri48Yxj4ZQopwa+wqwDi8PS0KxNMhkikGDM0+U8I9OKnRvICCdOXvcC3jtuslfi+hKH0ah0XgDxU85b4PcAIeYY1+/qb5844SGevvKxNke2YjBlMePi/QS+TJf1PmXr038HHthY+vio3U5GzSldtenD5tmJbrShhUwj3nnPQ==",data=form_data) ##用post是因為他的request method是POST ##response為以data作為條件送出去後得到的結果

print(response.text)##看得到的資料的形式 ##這邊看是獲得完整html網頁

##對得到的資料作剖析

##網頁內容定位


