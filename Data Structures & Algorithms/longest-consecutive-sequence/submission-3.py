class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Time: O(n) 
        s = set(nums)
        ans = 0

        for n in s: 
            if (n-1) not in s: 
                temp = 1
                while (n + temp) in s: 
                    temp += 1

                ans = max(ans, temp)


        return ans
                    

