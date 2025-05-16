from calendar import c
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
      self.send_header("Content-type", self.CONTENT_TYPE_HTML)
      self.end_headers()
      if message:
        self.wfile.write(message.encode())
    
    def _send_200(self, message: str = ''):
      self.send_response(200)
      self.send_header("Content-type", self.CONTENT_TYPE_HTML)
      self.end_headers()
      if message:
        self.wfile.write(message.encode())
    
    def _send_unauthorized(self, message: str = ''):
      self.send_response(401)
      self.send_header("Content-type", self.CONTENT_TYPE_HTML)
      self.end_headers()
      if message:
        self.wfile.write(message.encode())
    
    def check_authorized(func):
      def check(self):
        try:
          api_key = self.key
          if self.headers.get('Authorization') == None:
            return self._send_unauthorized("Missing auth header")
          elif self.headers.get('Authorization') != 'Basic {}'.format(api_key):
            return self._send_unauthorized("Wrong username/password")
          return func(self)
        except Exception as e:
          self._send_400(f"Server error: {str(e)}")
          return
      return check
    
    def _request_data(self):
      content_length = int(self.headers['Content-Length'])
      post_data = self.rfile.read(content_length)
      return post_data

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

    @check_authorized
    def do_POST(self):
      post_data = self._request_data()
      try:
        c = json.loads(post_data)
        car = Car(c['id'], c['name'], c['manufacturer'], c['year'], c['price'])
        car_db[str(car.car_id)] = car
        self._send_200("Car created successfully")
      except json.JSONDecodeError:
        self._send_400("Invalid JSON format")
      except KeyError:
        self._send_400("Missing required field(s)")
      except Exception as e:
        self._send_400(f"server error: {str(e)}")
      self._send_200()

    @check_authorized
    def do_DELETE(self):
      car_id = self.path.removeprefix('/delete/')
      if car_id not in car_db:
        self._send_400('id not found')
        return 
      del car_db[car_id]
      self._send_200()

    @check_authorized
    def do_PATCH(self):
      req_data = self._request_data()
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
    
    def do_PUT(self):
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

    
if __name__ == "__main__":
    simple_server = HTTPServer((HOST,PORT), SimpleServer)
    SimpleServer.set_api_key('dimik', 'Python')
    print("Starting server...")
    try:
        simple_server.serve_forever()
    except KeyboardInterrupt:
        pass
    simple_server.server_close()
    print("Server shutting down.")