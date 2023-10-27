import heapq
import collections

nums = [1, 2, 3, 1, 3, 1]

k = 2

# Step 1: Count the frequency of each element
frequency_map = collections.Counter(nums)

# Step 2: Create a max-heap based on the frequencies
max_heap = [(-freq, num) for num, freq in frequency_map.items()]
heapq.heapify(max_heap)

# Step 3: Extract the top k frequent elements from the max-heap
result = [heapq.heappop(max_heap)[1] for _ in range(k)]

print(result)
print(result)
print(result)
