import time
import threading

# def sleep_fnc(sec=1.1):
#   print("Inside sleep_fnc")
#   time.sleep(sec)

# t1 = time.perf_counter()
# thread_list = [threading.Thread(target=sleep_fnc) for _ in range(5)]
# for th in thread_list:
#   th.start()
# for th in thread_list:
#   th.join()
# t2 = time.perf_counter()
# time_spent = t2 - t1
# print(round(time_spent, 2))

def computer_fun():
  print("Inside computer_fun")
  for x in range(10000000):
    _ = pow(x, 123)
  print("finished computer")
t1 = time.perf_counter()
thread_list = [threading.Thread(target=computer_fun) for _ in range(5)]
for th in thread_list:
  th.start()
for th in thread_list:
  th.join()
t2 = time.perf_counter()
time_spent = t2 - t1
print(round(time_spent, 2))