import math


def minEatingSpeed(piles, h: int) -> int:
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (l + r) // 2

        totalTime = 0
        for p in piles:
            totalTime += math.ceil(float(p) / k)
        if totalTime <= h:
            res = k
            r = k - 1
        else:
            l = k + 1
    return res


if __name__ == '__main__':
    piles = [312884470]
    h = 968709470
    minEatingSpeed(piles,h)
