class Solution:
    def trap(self, height: List[int]) -> int:
        l, r, res = 0, len(height) - 1, 0
        l_max, r_max = height[l], height[r]
        
        while l < r: 
            if l_max > r_max: 
                r -= 1
                r_max = max(r_max, height[r])
                res += r_max - height[r]

            else: # l_max <= r_max
                l += 1
                l_max = max(l_max, height[l])
                res += l_max - height[l]

        return res