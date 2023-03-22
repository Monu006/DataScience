import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

search = "Dabur%20Honey"
flipKart_url = "https://www.flipkart.com/search?q="+ search
print(flipKart_url)
urlclient = urlopen(flipKart_url)


flipkart_html = bs(urlclient.read(), 'html.parser')

bigbox = flipkart_html.find_all('div',{"class":"_13oc-S"})

print(bigbox[0])


print(data)




