from socket import *

HOST = "localhost"
PORT = 8888

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("localhost", 8888))
server_socket.listen(5)

try:
  server_socket = socket(AF_INET, SOCK_STREAM)
  server_socket.bind((HOST, PORT))
  server_socket.listen(5)
  print("Server listening on port %s ..." % PORT)
  while True:
    client_socket, address = server_socket.accept()
    print("I got a connection from %s" % str(address))
    request_data = client_socket.recv(1024)
    request_data = request_data.decode()
    print()
    print("Request data:")
    print(request_data)

    response_data = "HTTP/1.1 200 OK\n\r"
    response_data += "Content-Type: text/html; charset=utf-8\n\r"
    response_data += "<html><body><h1>Hello World!"
    response_data += "</h1></body></html>\r\n\r\n"
    response_data = response_data.encode()
    client_socket.sendall(response_data)
    client_socket.shutdown(SHUT_RDWR)
except Exception as e:
  print(e)