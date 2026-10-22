class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid


            if nums[l] <= nums[mid]: # L is sorted
                if nums[l] <= target and target < nums[mid]: # nums[l] <= target < nums[mid]
                    r = mid - 1
                else: # target < nums[l] OR target >= nums[mid]
                    l = mid + 1
            else: # R is sorted
                if nums[mid] < target and target <= nums[r]: 
                    l = mid + 1
                else: 
                    r = mid - 1

        return -1