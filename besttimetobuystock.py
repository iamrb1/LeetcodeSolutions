def maxProfit(prices) :
    max_p = 0
    min_p = prices[0]

    n = len(prices)

    for i in range(1, n):
        max_p = max(prices[i] - min_p, max_p)
        min_p = min(prices[i], min_p)

    return max_p
if __name__ == '__main__':
    s = [7,1,5,3,6,4]
    s = maxProfit(s)
    print(s)