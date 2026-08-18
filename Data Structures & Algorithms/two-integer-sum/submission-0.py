class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers = {}

        for i, num in enumerate(nums):
            req_num = target - num
            if req_num in seen_numbers:
                return [seen_numbers[req_num], i]
            else:
                seen_numbers[num] = i
        

        