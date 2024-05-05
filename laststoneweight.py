import heapq
def lastStoneWeight(stones):
    for i, s in enumerate(stones):
        stones[i] = -s
    heapq.heapify(stones)
    while stones:
        s1 = -heapq.heappop(stones)
        if not stones:
            return s1
        s2 = -heapq.heappop(stones)
        if s1 > s2:
            heapq.heappush(stones, s2 - s1)
    return 0

if __name__ == '__main__':
    stones = [7,5,6,9,10,5]
    print(lastStoneWeight(stones))