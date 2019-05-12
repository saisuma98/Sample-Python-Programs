import urllib.request as rq
import re

url = 'https://www.google.com'
fHand = rq.urlopen(url)

for line in fHand:
    #print(line)
    links = re.findall(b'href="[http://].+?"', line)
    #print(len(links))
    for l in links:
        print(l.decode())
