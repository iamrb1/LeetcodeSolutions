def equalPairs(grid) -> int:
    columns = {}
    i = 0
    j = 0
    count = 0
    while j < len(grid[0]):
        col = []
        while i < len(grid[0]):
            col.append(grid[i][j])
            i += 1
        columns[count] = col
        count += 1
        j += 1
        i = 0
    count = 0
    d = list(columns.values())
    for row in grid:
        for col in d:
            if row == col:
                count += 1
    return count



if __name__ == '__main__':
    grid = [[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]
    print(equalPairs(grid))