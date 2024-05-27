import requests as re
from bs4 import BeautifulSoup as bea

res = re.get("https://vacations.ctrip.com/list/freetravel/d-xian-7.html?p=1&startcity=5152#_flta") ##觀察到p=1為當前網頁頁面參數
for i in range(1,9): #do 1~8
  print("\n第"+str(i)+"頁\n")
  url = "https://vacations.ctrip.com/list/freetravel/d-xian-7.html?p=x&startcity=5152#_flta" ##數字用x取代，後面用replace
  url = url.replace('x',str(i))
  res = re.get(url)

  soup = bea(res.text, 'html.parser')
  #soup

  titles = soup.select('.list_product_title span')
  #print(type(titles))
  for k in titles :
    print(k.get_text()) ##.text應該看官網應該只能用在內部? 盡量使用.get_text()方法取代!!
  
