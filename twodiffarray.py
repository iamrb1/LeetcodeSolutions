def findDifference(nums1, nums2):
        s_n1, s_n2 = set(), set()
        a1, a2 = [], []
        for ele in nums1:
            if ele not in nums2:
                if ele not in s_n1:
                    a1.append(ele)
                    s_n1.add(ele)

        for ele in nums2:
            if ele not in nums1:
                if ele not in s_n2:
                    a2.append(ele)
                    s_n2.add(ele)

        return [a1, a2]
if __name__ == '__main__':
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    print(findDifference(nums1,nums2))