class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, res, bucket = 0, 0, 0, set()

        while r < len(s): 
            while s[r] in bucket: 
                bucket.remove(s[l])
                l += 1
            bucket.add(s[r])
            res = max(res, r - l + 1)
            r += 1


        return res
