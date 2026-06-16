class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        l, r = 0, m * n

        while l < r:
            m = (l + r) // 2

            val = matrix[m // n][m % n]

            if val < target:
                l = m + 1
            elif val > target:
                r = m
            else:
                return True
            
        
        return False