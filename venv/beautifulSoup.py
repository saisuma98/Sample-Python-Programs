from bs4 import BeautifulSoup
import urllib.request as rq
import ssl


#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.google.com'
html = rq.urlopen(url).read()
#pat = r'href="[http://].+?"'

soup = BeautifulSoup(html,"html.parser")
tags = soup('script')
for t in tags:
    print(t)




