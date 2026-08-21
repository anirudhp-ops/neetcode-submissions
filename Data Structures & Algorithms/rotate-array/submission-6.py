"""

Understanding: 



Initial Solution:





Optimal Solution: 

Edge Cases: 



"""



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        nums.reverse()

        first_start = 0 
        first_end = k - 1

        second_start = k 
        second_end = len(nums) - 1 
        
        while first_start < first_end: 
            nums[first_start], nums[first_end] = nums[first_end], nums[first_start]
            first_start += 1 
            first_end -= 1 
        
        while second_start < second_end:
            
            nums[second_start], nums[second_end] = nums[second_end], nums[second_start]
            second_start += 1 
            second_end -= 1 

 

        