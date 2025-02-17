#215. Kth Largest Element in an Array
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
    
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)  # Sort in descending order
        return nums[k - 1]
    
f = Solution()
a = [3,2,1,5,6,4]
k =2
print(f.findKthLargest(a, k))