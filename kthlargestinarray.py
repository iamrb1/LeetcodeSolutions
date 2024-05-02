import heapq
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heap = []
        for ele in nums:
            heapq.heappush(heap, -ele)
        i = 0
        while i < k - 1:
            heapq.heappop(heap)
            i += 1
        return -1*heap[0]