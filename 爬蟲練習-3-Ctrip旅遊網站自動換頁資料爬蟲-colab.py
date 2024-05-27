import requests as re
from bs4 import BeautifulSoup as bea

res = re.get("https://vacations.ctrip.com/list/freetravel/d-xian-7.html?p=1&startcity=5152#_flta")


soup = bea(res.text, 'html.parser')
#soup

titles = soup.select('.list_product_title span')
#print(type(titles))
for i in titles :
  print(i.get_text()) ##.text應該看官網應該只能用在內部? 盡量使用.get_text()方法取代!!
