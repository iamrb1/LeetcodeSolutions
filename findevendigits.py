def findNumbers(nums) -> int:
    count = 0

    for ele in nums:
        ele = str(ele)
        l = len(ele)
        if l % 2 == 0:
            count += 1

    return count

if __name__ == '__main__':
    bob = [555,901,482,1771]
    bob = findNumbers(bob)