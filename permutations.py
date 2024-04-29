def permute(nums):
    def backtrack(curr):
        if len(curr) == len(nums):
            ans.append(curr[:])
            return

        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()

    ans = []
    backtrack([])
    return ans



if __name__ == '__main__':
    bob = permute([1,2,3])
    print(bob)