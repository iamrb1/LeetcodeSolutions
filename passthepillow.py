class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        start = 1
        tick = 1
        while time != 0:
            if start == 1:
                tick = 1
            if start == n:
                tick = -1
            start += tick
            time -= 1
        return start

