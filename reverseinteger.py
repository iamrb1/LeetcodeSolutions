def reverse(x: int) -> int:
    if x * -1 > 0:
        s = '-' + str(-1*x)[::-1]
        x = int(s)
    else:
        x = int(str(x)[::-1])
    if x > 2 ** 31 or x < -1 * (2 ** 31):
        return 0
    else:
        return x

if __name__ == '__main__':
    x = 1234236467
    reverse(x)
