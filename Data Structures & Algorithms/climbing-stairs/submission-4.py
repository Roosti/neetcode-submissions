class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 0, 1
        if n <= 2:
            return n
        else:
            for i in range(n):
                temp = one + two
                one = two
                two = temp
        return two