def findKthPositive(arr, k):
    n = len(arr) + k
    hmap = {}
    for i in range(1, n + 1):
        hmap[i] = i

    for i in range(len(arr)):
        if arr[i] in hmap:
            del hmap[arr[i]]
    l = list(hmap.values())

    return l[k - 1]

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    k = 2
    arr = findKthPositive(arr, k)
    print(arr)