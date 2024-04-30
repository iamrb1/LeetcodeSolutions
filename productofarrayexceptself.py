def productExceptSelf(nums):
    count = nums.count(0)
    if count == len(nums):
        return nums
    lp = 1
    rp = 1
    result = []
    for i in range(len(nums)):
        result.append(lp)
        lp *= nums[i]
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= rp
        rp *= nums[i]

    return result




if __name__ == '__main__':
    nums = [2,3,0,0]
    print(productExceptSelf(nums))