import requests
import json

def create_car():
    car2 = {
        "id": 2,
        "name": "BMW",
        "manufacturer": "Germany",
        "year": 2020,
        "price": 100000
    }
    
    url = "http://localhost:8888"
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(
            url,
            data=json.dumps(car2),  
            headers=headers,        
            auth=('dimik', 'Python')
        )
        print(response.status_code)
        print(response.content)
        if response.status_code == 200:
            print("New car created with id", car2['id'])
        print()
    except requests.exceptions.RequestException as e:
        print("Error creating car:", e)
  
def get_car(car_id):
  url =  "http://localhost:8888"
  params = {'id': car_id}
  response = requests.get(url, params)
  print(response.status_code)
  print(response.text)

def update_car(car_id, price):
  print("updating_car")
  url = 'http://localhost:8888'
  car = {"id": car_id, "price": price}
  response = requests.patch(url, data=json.dumps(car), auth=('dimik', 'Python'))
  print(response.status_code)
  print(response.content)

if __name__ == "__main__":
  print("creating cars")
  create_car()
  get_car(2)
  update_car(2, 1000000)
  get_car(2)
  
