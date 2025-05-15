import multiprocessing
import time
def computer_fun():
  print("Inside computer_fun")
  for x in range(10000000):
    _ = pow(x, 2)
  print("finished computer")

if __name__ == "__main__":
  t1 = time.perf_counter()
  process_list = [
    multiprocessing.Process(target=computer_fun) for _ in range(5)
  ]
  for p in process_list:
    p.start()
  for p in process_list:
    p.join()
  t2 = time.perf_counter()
  time_spent = t2 - t1
  print(round(time_spent, 2))

