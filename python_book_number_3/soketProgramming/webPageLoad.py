import socket

HOST = "subeen.com"
PORT = 80

s = socket.socket()
s.connect((HOST, PORT))
command = 'GET /files/a.txt HTTP/1.1\nHost: subeen.com\nConnection: close\n\n'
s.send(command.encode())
while True:
  data = s.recv(1024)
  if data == b'':
    break
  print(data.decode())
s.close()