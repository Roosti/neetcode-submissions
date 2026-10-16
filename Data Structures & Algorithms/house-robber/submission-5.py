class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        i, j = 0, 0

        for n in nums:
            tmp = max(i + n, j)
            i = j
            j = tmp
        return tmp
        """

        #dp?
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for n in range(2, len(nums)):
            dp[n] = max(dp[n-1], dp[n-2] + nums[n])
        
        return dp[-1]