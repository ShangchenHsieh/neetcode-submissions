class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, m, r = 0, 0, len(matrix) - 1

        while l <= r: 
            m = (l + r) // 2
            if target > matrix[m][-1]: 
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else: 
                break

        l, m_2, r = 0, 0, len(matrix[0]) - 1

        while l <= r: 
            m_2 = (l + r) // 2
            if target > matrix[m][m_2]: 
                l = m_2 + 1
            elif target < matrix[m][m_2]:
                r = m_2 - 1
            else: 
                return True

        return False 
