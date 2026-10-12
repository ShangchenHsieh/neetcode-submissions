class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = [] # (index, height)
        res = 0 

        for i, h in enumerate(heights): 
            start = i
            while s and h < s[-1][1]: 
                temp = s.pop() 
                start = temp[0]
                res = max(res, temp[1] * (i - temp[0]))
            s.append((start, h))

        # still some bars that can extend all the way to the end of the histogram 
        for i, h in s: 
            res = max(res, (len(heights) - i) * h)
        return res