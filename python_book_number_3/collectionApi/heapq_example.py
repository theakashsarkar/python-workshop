from typing import List
import heapq

def find_kth_largest(nums: List[int], k: int) -> int:
  heap = []
  for num in nums:
    heapq.heappush(heap, num * -1)
  for _ in range(k - 1):
    heapq.heappop(heap)
  return heap[0] * -1
if __name__ == "__main__":
  nums = [3, 2, 1, 5, 6, 4]
  k = 2
  # print(find_kth_largest(nums, k))

class MaxHeap:
  def __init__(self, items = []):
    self.heap = [x * -1 for x in items]
    if items:
      heapq.heapify(self.heap)
  def __len__(self):
    return len(self.heap)
  
  def push(self, item):
    heapq.heappush(self.heap, item * -1)
  def pop(self):
    return heapq.heappop(self.heap) * -1
  def look(self):
    return self.heap[0] * -1
if __name__ == "__main__":
  nums = [3, 2, 1, 5, 6, 4]
  max_heap = MaxHeap()
  for item in nums:
    max_heap.push(item)
  li = [max_heap.pop() for _ in range(len(max_heap))]
  print(li)
  # max_heap.push(10)
  # max_heap.push(11)
  # print(max_heap.look())