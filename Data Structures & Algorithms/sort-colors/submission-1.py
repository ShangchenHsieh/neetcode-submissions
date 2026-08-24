class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Noticed inputs are just 0, 1, 2
        Intuition: counter
        """
        
        counter = [0 for _ in range(3)]
        
        for n in nums: 
            counter[n] += 1 # 1 2 1
        
        # 0 1 1 2
        

        j = 0
        for i in range(3): # iterate through the counter
            while counter[i] != 0: # modify the number to the desire amount
                nums[j] = i
                j += 1
                counter[i] -= 1 
