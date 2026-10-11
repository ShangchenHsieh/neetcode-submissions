class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(n log n)
        res = []

        for i in range(len(nums)): 

            if nums[i] > 0: # we can stop b/c the whole array is sorted 
                break
            
            if i != 0 and nums[i] == nums[i - 1]: # duplicate
                continue

            l, r = i + 1, len(nums) - 1

            while l < r: 
                threesum = nums[i] + nums[l] + nums[r]
                if threesum > 0: 
                    r -= 1
                elif threesum < 0: 
                    l += 1
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]: 
                        l += 1


        return res


        