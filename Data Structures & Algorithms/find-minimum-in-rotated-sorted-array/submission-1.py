class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1 

        # start at the ends 
        # find the midpoint 
        # 
        #
        #
        #
        #
        if len(nums) == 1: 
            return nums[0]
        
        while left < right: 

            mid = left + (right - left) // 2 

            if nums[left] < nums[right]: 
                return nums[left]
            
            elif right - left == 1: 
                return nums[right]

            if nums[mid] > nums[left] and nums[mid] > nums[right]: 
                left = mid
            
            elif nums[mid] < nums[left] and nums[mid] < nums[right]: 
                right = mid 
            
        

        return right

            




        