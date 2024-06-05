def partitionString(s: str):
    d = {}
    c = 0
    temp = []
    for ch in s:
        if ch in temp:
            d[c] = temp
            c += 1
            temp = [ch]
        else:
            temp.append(ch)
    if d:
        total = len(d.values())
        return total + len(temp)
    else:
        if temp:
            return 1


if __name__ == '__main__':
    s = "cuieokbs"
    print(partitionString(s))