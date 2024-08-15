def productExceptSelf(nums):
    pr = 1
    po = 1
    pre = []
    post = []
    res = []
    for ele in nums:
        pr *= ele
        pre.append(pr)
    for ele in nums[::-1]:
        po *= ele
        post.append(po)
    post = post[::-1]
    for i in range(len(nums)):
        if i == 0:
            res.append(1 * post[i + 1])
        elif i == len(nums) - 1:
            res.append(pre[i - 1] * 1)
        else:
            res.append(pre[i - 1] * post[i + 1])
    return res

if __name__ == '__main__':
    nums = [1,2,4,6]
    productExceptSelf(nums)