class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i, j = 0, len(heights) - 1
        while i < j:
            w = (j - i)
            h = min(heights[i], heights[j])
            area = w * h
            res = max(res, area)
            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
        return res