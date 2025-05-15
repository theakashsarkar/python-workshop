import requests
import json

def create_car():
  car2 = {
    "id" : "2",
    "name" : "BMW",
    "manufacturer" : "Germany",
    "year" : "2020",
    "price" : "100000"
  }
  car3 = {
    "id" : "3",
    "name" : "Audi",
    "manufacturer" : "Germany",
    "year" : "2020",
    "price" : "100000"
  }
  car4 = {
    "id" : "4",
    "name" : "Mercedes",
    "manufacturer" : "Germany",
    "year" : "2020",
    "price" : "100000"
  }
  url = "http://localhost:8888"
  for car in [car2, car3, car4]:
   response = requests.post(url, data=json.dumps(car))
   print(car)
   print(response.status_code)
   if response.status_code == 200:
     print("Car created successfully")
   print()
  
def get_car(car_id):
  url =  "http://localhost:8888"
  params = {'id': car_id}
  response = requests.get(url, params)
  print(response.status_code)
  print(response.text)

if __name__ == "__main__":
  print("creating cars")
  create_car()
  for i in range(1, 5):
    print("getting car with id {}".format(i))
    get_car(i)
    
