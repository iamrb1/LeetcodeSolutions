def canPlaceFlowers(flowerbed, n: int) -> bool:
    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
            empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
            if empty_left_plot and empty_right_lot:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True

    return count >= n

if __name__ == '__main__':
    flowerbed = [0,0,1,0,1]
    n = 1
    print(canPlaceFlowers(flowerbed, n))