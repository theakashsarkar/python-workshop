from http.server import HTTPServer, BaseHTTPRequestHandler
from dataclasses import dataclass
from urllib.parse import urlparse, parse_qs
import json
import base64

@dataclass
class Car:
  car_id: int
  name: str
  manufacturer: str
  year: int
  price:int
car_db = dict()
HOST, PORT = "localhost", 8888

class SimpleServer(BaseHTTPRequestHandler):
    
    CONTENT_TYPE_HTML = "text/html"


    
    @classmethod
    def set_api_key(cls, username, password):
      key_str = '{}:{}'.format(username, password)
      cls.key = base64.b64encode(key_str.encode('utf-8')).decode()
    def _send_400(self, message: str = ''):
      self.send_response(400)
      self.send_header("Content-type", CONTENT_TYPE_HTML)
      self.end_headers()
      self.wfile.write(message.encode())
    
    def _send_200(self, message: str = ''):
      self.send_response(200)
      self.send_header("Content-type", CONTENT_TYPE_HTML)
      self.end_headers()
      self.wfile.write(message.encode())
    
    def _send_unauthorized(self, message: str = ''):
      self.send_response(401)
      self.send_header("Content-type", CONTENT_TYPE_HTML)
      self.end_headers()
      self.wfile.write(message.encode())

    def do_GET(self):
        parsed_url = urlparse(self.path)
        qs = parse_qs(parsed_url.query)
        if 'id' not in qs or len(qs['id']) == 0:
          self._send_400()
          html_content = "<html><body>id missing</body></html>"
          self.wfile.write(bytes(html_content, "utf-8"))
          return 
        try:
         car_id = int(qs['id'][0])
         car = car_db[str(car_id)]
         self._send_200()
         details = "Car Name: {}<br>Manufacturer: {}<br>Year: {}"
         details += "<br>Price: {}" 
         details = details.format(car.name, car.manufacturer, car.year, car.price)
         html_content = "<html><body>{}</body></html>".format(details)
         self.wfile.write(bytes(html_content, "utf-8"))
        except (ValueError, KeyError):
         self._send_400()
         html_content = "<html><body><h1>Invalid id</h1></body></html>"
         self.wfile.write(bytes(html_content, "utf-8"))

    def do_POST(self):
      api_key = SimpleServer.key
      if self.headers.get('Authorization') == None:
        return self._send_unauthorized("Missing auth header")
      elif self.headers.get('Authorization') != "Basic {}".format(api_key):
        return self._send_unauthorized("Wrong username/password")
      content_length = int(self.headers['Content-Length'])
      post_data = self.rfile.read(content_length)
      try:
        c = json.loads(post_data)
        car = Car(c['id'], c['name'], c['manufacturer'], c['year'], c['price'])
        car_db[car.car_id] = car
      except KeyError:
        self._send_400()
        html_content = "<html><body><h1>Missing required field(s)"
        html_content += "</h1></body></html>"
        self.wfile.write(bytes(html_content, "utf-8"))
        return
      self._send_200()

    def do_DELETE(self):
      car_id = self.path.removeprefix('/delete/')
      if car_id not in car_db:
        self._send_400('id not found')
        return 
      del car_db[car_id]
      self._send_200()
    
    def do_PATCH(self):
      content_length = int(self.headers['Content-Length'])
      req_data = self.rfile.read(content_length)
      try:
        c = json.loads(req_data)
        if 'id' not in c:
          self._send_400('id missing')
          return 
        car = car_db[c["id"]]
        for key in c:
          car.__setattr__(key, c[key])
        car_db[car.car_id] = car
      except KeyError:
        self._send_400('Invalid field(s)')
        return
      self._send_200()
      self.wfile.write(b'car update')
      return

    
if __name__ == "__main__":
    car = Car(1, "Ferrari", "Spider", 2020, 1000000000)
    car_db[car.car_id] = car
    simple_server = HTTPServer((HOST,PORT), SimpleServer)
    print(f"Server started on http://{HOST}:{PORT}")
    try:
        simple_server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down the server...")
        simple_server.server_close()