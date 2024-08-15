def dailyTemperatures(temperatures):
    stack = [temperatures[0]]
    output = []
    count = 0
    i = 1
    while stack:
        t = stack.pop()
        if t < temperatures[i]:
            stack.append(temperatures[i])
            count += 1
            output.append(count)
            count = 0
        else:
            s = []
            while 
    return output

if __name__ == '__main__':
    temperatures = [30, 38, 30, 36, 35, 40, 28]
    dailyTemperatures(temperatures)