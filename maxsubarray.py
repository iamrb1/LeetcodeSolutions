class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        m = sum(nums[:k])
        c = m
        for i in range(k, len(nums)):
            c += nums[i] - nums[i - k]
            m = max(m,c)
        return m/k