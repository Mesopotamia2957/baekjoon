import sys
import heapq

input = sys.stdin.readline
N = int(input())

max_heap = [] # 중간값 보다 작거나 같은 값
min_heap = [] # 중간값 보다 큰 값
output = []

for _ in range(N):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if min_heap and -max_heap[0] > min_heap[0]:
        min_heap_root = heapq.heappop(min_heap)
        max_heap_root = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, max_heap_root)
        heapq.heappush(max_heap, -min_heap_root)

    output.append(str(-max_heap[0]))

print("\n".join(output))
