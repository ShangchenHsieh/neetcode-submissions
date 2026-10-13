class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, res = 0, 0
        char = set() 

        for r in range(len(s)): 
            while s[r] in char: 
                char.remove(s[l])
                l += 1
            char.add(s[r])
            res = max(res, r - l + 1)

        return res