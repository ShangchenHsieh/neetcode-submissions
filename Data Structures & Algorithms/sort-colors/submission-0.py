class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def merge(arr: list[int], left: int, m: int, right: int):
            left_arr, right_arr = arr[left:m+1], arr[m+1:right+1]
            i, j, k = 0, 0, left

            while i < len(left_arr) and j < len(right_arr): 
                if left_arr[i] >= right_arr[j]: 
                    arr[k] = right_arr[j]
                    j += 1
                else: 
                    arr[k] = left_arr[i]
                    i += 1

                k += 1
            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1

            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1
            

        def mergeSort(array: list, left: int, right: int) -> Optional["list[int]"]: # divide and conquer
            if left == right: 
                return array
            
            m = (left + right) // 2
            # left part 
            mergeSort(array, left, m)
            # right part 
            mergeSort(array, m+1, right)
            # and then merge at the end
            merge(array, left, m, right)

        mergeSort(nums, 0, len(nums)-1)