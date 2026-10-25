class Solution:
    def rob(self, nums: List[int]) -> int:
        cum = nums

        return max(cum[0], self.jerk_off(cum[1:]), self.jerk_off(cum[:-1]))

    def jerk_off(self, cum):
        penis_1, penis_2 = 0, 0
        for sperm in cum:
            super_penis = max(penis_1 + sperm, penis_2)
            penis_1 = penis_2
            penis_2 = super_penis
        return penis_2