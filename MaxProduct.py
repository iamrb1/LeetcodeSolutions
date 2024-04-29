def maxProduct(nums) -> int:
    currmax = nums[0]
    currmin = nums[0]
    res = nums[0]
    for i in range(1, len(nums)):
        t = currmax
        currmax = max(nums[i], nums[i] * currmax, nums[i] * currmin)
        currmin = min(nums[i], nums[i] * t, nums[i] * currmin)
        res = max(res, currmax)
    return res

if __name__ == '__main__':
    bob = [2,3,-2,4]
    bob = maxProduct(bob)
