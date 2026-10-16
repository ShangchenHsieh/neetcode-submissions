class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r, m = 0, len(matrix) - 1, 0

        while l <= r: 
            m = (l + r) // 2
            if matrix[m][0] > target: 
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else: # if it happens to be the target
                break

        l, r, row_m = 0, len(matrix[0]) - 1, 0

        while l <= r: 
            row_m = (l + r) // 2
            if matrix[m][row_m] > target: 
                r = row_m - 1
            elif matrix[m][row_m] < target:
                l = row_m + 1
            else: # if it happens to be the target
                return True
        
        return False