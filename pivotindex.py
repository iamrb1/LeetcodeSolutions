def pivotIndex(nums) -> int:
    for i in range(len(nums)):
        l = nums[:i]
        r = nums[i+1:]
        if sum(l) == sum(r):
            return i
    return -1

if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    print(pivotIndex(nums))