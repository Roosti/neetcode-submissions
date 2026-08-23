class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_seq = 0

        for num in num_set:
            if (num - 1) not in num_set:
                curr_length = 0
                while (num + curr_length) in num_set:
                    curr_length += 1
                if curr_length > max_seq:
                    max_seq = curr_length
        return max_seq