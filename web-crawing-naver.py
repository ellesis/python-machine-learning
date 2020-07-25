import requests
from bs4 import BeautifulSoup
import datetime

dtnow = datetime.datetime.now()
print("{} Rignt Now Naver Realtime searching words Top 20".format(dtnow))

naver_html = requests.get('https://www.naver.com/')
html = naver_html.text

soup = BeautifulSoup(html,'html.parser')
words = soup.findAll('span',{'class':'ah_k'})
print(words)

for i in range(20):
    print('Top {0:2d} => {1}'.format(i+1,words[i].text))
