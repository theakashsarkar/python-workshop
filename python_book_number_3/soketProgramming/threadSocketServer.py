import socket
import threading
import socketserver

class ThreadTcpRequestHandler(socketserver.BaseRequestHandler):
  def handle(self):
    data  = self.request.recv(1024)
    cur_thread = threading.current_thread()
    response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
    self.request.sendall(response)

class ThreadTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
  pass
def client(ip, port, message):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((ip, port))
    sock.sendall(bytes(message, 'ascii'))
    response = str(sock.recv(1024), 'ascii')
    print("Received: {}".format(response))
if __name__ == "__main__":
  # Port 0 means to select an arbitrary unused port
  HOST, PORT = "localhost", 0
  server = ThreadTCPServer((HOST, PORT), ThreadTcpRequestHandler)
  with server:
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)
    client(ip, port, "Hello World 1")
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")
    server.shutdown()