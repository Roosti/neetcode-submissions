class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        bucket_array = [[] for _ in range(len(nums) + 1)]
        ans = []

        for num in nums:
            num_count[num] = 1 + num_count.get(num, 0)
        
        for num, count in num_count.items():
            bucket_array[count].append(num)
        
        for i in range(len(bucket_array) - 1, 0, -1):
            for num in bucket_array[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return ans