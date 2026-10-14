class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = set(s) # each char in s
        res = 0

        for c in char: 
            l, count = 0, 0
            
            for r in range(len(s)): 
                if s[r] == c: # if the s[r] is the same as the currently selected char
                    count += 1
                
                while (r - l + 1) - count > k: # more char need to be replaced
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                res = max(res, r - l + 1)
        return res