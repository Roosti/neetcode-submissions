class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_numbers = set()
        for num in nums:
            if num not in seen_numbers:
                seen_numbers.add(num)
            else:
                return True
        return False