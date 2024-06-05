def kthFactor(n: int, k: int) -> int:
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    if k > len(factors):
        return -1
    else:
        return factors[k - 1]

if __name__ == '__main__':
    n = 7
    k = 2
    print(kthFactor(7,2))
