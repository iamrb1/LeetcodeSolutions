def generate(numRows: int) :
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]
    if numRows == 3:
        return [[1], [1, 1], [1, 2, 1]]

    l = [[1], [1, 1], [1, 2, 1]]
    for i in range(3, numRows):
        new_l = []
        last = l[-1]
        j = 0
        while j < len(last):
            if j == 0:
                new_l.append(1)
            elif j == len(last) - 1:
                new_l.append((last[j - 1]) + 1)
                new_l.append(1)
            else:
                new_l.append((last[j - 1]) + last[j])
            j += 1
        l.append(new_l)
    return l

if __name__ == '__main__':
    numRows = 5
    generate(numRows)