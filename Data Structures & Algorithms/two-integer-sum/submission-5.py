class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp_map = {}
        for i in range(len(nums)): 
            if nums[i] in comp_map: 
                return [comp_map[nums[i]], i]
            else: 
                comp_map[target - nums[i]] = i
