def twoSum(numbers, target: int):
    i = 0
    j = len(numbers) - 1
    while i < len(numbers):
        first = numbers[i]
        second = numbers[j]
        if first + second == target:
            return [i + 1, j + 1]
        elif first + second < target:
            i += 1
        else:
            j -= 1

if __name__ == '__main__':
    numbers = [5,25,75]
    target = 100
    twoSum(numbers,target)