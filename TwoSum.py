def twoSum(nums, target):
    Dict = {}
    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in Dict:
            return [i, Dict[compliment]]
        Dict[nums[i]] = i

if __name__ == '__main__':
    bob = [2,7,11,15]
    bob = twoSum(bob, 9)
    print(bob)