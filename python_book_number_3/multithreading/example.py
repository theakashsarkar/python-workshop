import time

def sleep_fnc(sec=1.1):
  print("inside sleep_fnc")
  time.sleep(sec)

def compute_fnc():
  print("inside compute_fnc")
  for x in range(10000000):
    _ = pow(x, 123)
for fnc in [sleep_fnc, compute_fnc]:
  t1 = time.perf_counter()
  fnc()
  t2 = time.perf_counter()
  time_spent = t2 - t1
  print(round(time_spent, 2))