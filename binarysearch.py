def search(nums, target: int) -> int:
    low = 0
    high = len(nums)
    if target > nums[-1] or target < nums[0]:
        return -1
    while low <= high:
        mid = low + (high - low) // 2
        ele = nums[mid]
        if ele == target:
            return mid
        elif ele < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 13
    print(search(nums,target))