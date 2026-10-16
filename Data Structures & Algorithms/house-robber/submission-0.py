class Solution:
    def rob(self, nums: List[int]) -> int:
        i, j = 0, 0

        for n in nums:
            tmp = max(i + n, j)
            i = j
            j = tmp
        return tmp