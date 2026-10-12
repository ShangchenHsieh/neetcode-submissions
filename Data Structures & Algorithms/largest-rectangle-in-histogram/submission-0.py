class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [] # (index, height)
        res = 0 

        for i, h in enumerate(heights + [0]): 
            start = i
            while s and h < s[-1][1]: 
                temp = s.pop() 
                start = temp[0]
                res = max(res, temp[1] * (i - temp[0]))
            s.append((start, h))

        return res