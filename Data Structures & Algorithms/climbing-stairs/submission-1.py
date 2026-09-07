from functools import cache

class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        cache = [0] * (n + 1)
        if n <= 2:
            cache[n] = n
            return n
        else:
            return (self.climbStairs(n - 1) + (self.climbStairs(n - 2)))
        