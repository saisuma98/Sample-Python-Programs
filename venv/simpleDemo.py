import socket

#create

mySoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect
mySoc.connect(('www.google.com', 80))

cmd = 'GET http://www.google.com/ HTTP/1.0\r\n\r\n'.encode()
mySoc.send(cmd)


# receive

while True:
    data = mySoc.recv(512)
    if (len(data)<1):
        break

    print(data.decode())

print("done")




