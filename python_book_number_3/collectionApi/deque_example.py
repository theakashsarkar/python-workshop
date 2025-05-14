from collections import deque
# d = deque(maxlen = 3)
# d.append(1)
# d.append(2)
# d.append(3)
# print(d)
# d.extend([1,2,3,4,5])
# d.append(8)
# # d.popleft()
# d.appendleft(1)
# print(d)

# d = deque([1,2,3,4,5], maxlen = 5)
# d.appendleft(6)
# print(d)

# temp_q = deque(temp_list[:100], maxlen = 100)
# sum_temp = sum(temp_q)
# avg_temp = sum_temp / 100
# temp_q.append(next_temp)
# sum_temp += next_temp - temp_q.popleft()

def average_temp(temp_list, k = 100):
  temp_q = deque(temp_list[:k], maxlen = k)
  sum_temp = sum(temp_q)
  avg_temp = sum_temp / k
  print(temp_q.popleft())
  for next_temp in temp_list[k:]:
    sum_temp += next_temp - temp_q.popleft()
    temp_q.append(next_temp)
    avg_temp = sum_temp / k
  return avg_temp
avg_temp = average_temp([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 20)
print(avg_temp)