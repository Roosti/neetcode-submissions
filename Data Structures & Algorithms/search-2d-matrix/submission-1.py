class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        l, r = 0, m
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else: 
                break
        if not l <= r:
            return False
        target_row = (l + r) // 2
    
        l, r = 0, n
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[target_row][mid]:
                l = mid + 1
            elif target < matrix[target_row][mid]:
                r = mid - 1
            else:
                return True
        return False