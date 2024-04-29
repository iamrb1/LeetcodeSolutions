# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.



def nextGreaterElement(nums1, nums2):
    hashmap = {}
    ans = []
    for i in range(len(nums2)):
        hashmap[nums2[i]] = i

    for j in range(len(nums1)):
        ele = nums1[j]
        if ele in hashmap:
            try:
                if ele > nums2[hashmap.get(nums1[j]) + 1]:
                    ans.append(-1)
                else:
                    ans.append(nums2[hashmap.get(nums1[j]) + 1])
            except:
                ans.append(-1)
        else:
            ans.append(-1)

    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bob = nextGreaterElement([4,1,2], [1,3,4,2])
    print(bob)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
