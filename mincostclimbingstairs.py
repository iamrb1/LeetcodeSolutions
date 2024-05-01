def minCostClimbingStairs(cost) -> int:
    n = len(cost)
    for i in range(2, n):
        cost[i] += min(cost[i - 1], cost[i - 2])
    return min(cost[n - 1], cost[n - 2])

if __name__ == '__main__':
    cost = [0,0,1,1]
    print(minCostClimbingStairs(cost))