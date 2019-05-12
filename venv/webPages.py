import urllib.request as ur


#link1 = 'https://github.com/nasirbashak/Ball-Burst-Game/blob/master/Bullet.pde'
#link3 = 'https://github.com/nasirbashak/DBMS-Projects-A-sec/blob/master/hello.txt'

link2 = 'http://data.pr4e.org/romeo.txt'
fHand = ur.urlopen(link2)

for line in fHand:
    print(line.decode().strip())