import urllib3 as urllib
from bs4 import BeautifulSoup as bs
from fake_headers import Headers 

zoomurl = "https://zoom.us/support/download"
headers = Headers(browser="firefox", os="win", headers=True).generate()

# for i in range(10):
       # print(headers.generate())

http = urllib.PoolManager()
page = http.request('GET', zoomurl, headers=headers)
soup = bs(page.data, features="html.parser")
#check = soup.findAll('div')
check = soup.findAll('p', {"class": "setup-finger"}, recursive=True)
#print(soup.prettify())
print(check)

"""
html tags:
select id="linuxostype"
    option value="ubu"
"""
