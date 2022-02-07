from requests_html import HTMLSession
import requests
from bs4 import BeautifulSoup
 
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36', 'accept': '*/*'}

def get_html_with_JS(url):
    session = HTMLSession()
    
    # Use the object above to connect to needed webpage
    resp = session.get(url)
    
    # Run JavaScript code on webpage
    resp.html.render()
    r = resp.html.html
    return  r


def get_html_without_JS(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    print('url', url)
    r = r.text
    return r


url = 'https://themewagon.com/theme-price/free'
soup = BeautifulSoup(get_html_with_JS(url), "html.parser")



print(soup.select_one('.next.page-numbers.page-link'))
# with open('data.txt', "w", encoding="utf-8") as f:
#     f.write(str(soup))
# print(soup)
# print("\r\n"*10)
# with open('data.txt', 'r') as file:
#     data = file.read().rstrip()
#     soup = BeautifulSoup(data, "html.parser")
# find(class_="next page-numbers page-link")
# find('next page-numbers page-link')
