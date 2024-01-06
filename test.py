import requests
from bs4 import BeautifulSoup

url = 'https://www.aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=7396'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

bookservices = soup.select('.bo3')
for no, book in enumerate(bookservices, 1):
    print(no, book.text.strip())
