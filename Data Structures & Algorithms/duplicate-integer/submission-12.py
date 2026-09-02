class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)

        return not (len(nums) == len(s))