
def asteroidCollision(asteroids):
    stack = []
    for asteroid in asteroids:
        if asteroid > 0:
            stack.append(asteroid)
        else:
            while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                stack.pop()
            if not stack or stack[-1] < 0:
                stack.append(asteroid)
            elif stack[-1] == abs(asteroid):
                stack.pop()
    return stack

if __name__ == '__main__':
    asteroids = [10,2,-5]
    print(asteroidCollision(asteroids))