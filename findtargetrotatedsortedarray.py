def search(nums, target: int) -> int:
    def bs(nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
    l = 0
    r = len(nums) - 1
    pivot = 999
    while l <= r:
        m = (l + r) // 2
        if nums[m] > nums[m-1] and nums[m + 1] < nums[m]:
            pivot = m
            break
        if r < len(nums) - 1:
            if nums[r] > nums[r-1] and nums[r + 1] < nums[r]:
                pivot = r
                break
        if l > 0:
            if nums[l] > nums[l - 1] and nums[l + 1] < nums[l]:
                pivot = l
                break

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m - 1
    if pivot != 999:
        new_l = nums[pivot+1:]
        new_r = nums[:pivot+1]
        r = bs(new_r,target)
        if r != -1:
            return r
        l = bs(new_l,target)
        if l != -1:
            return len(new_r) + l
    else:
        return bs(nums,target)
    return -1


if __name__ == '__main__':
    nums = [1,3,5]
    target = 0
    print(search(nums,target))