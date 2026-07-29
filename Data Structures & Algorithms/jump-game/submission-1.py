class Solution:
    def canJump(self, nums: List[int]) -> bool:
        status = 0 

        for i in range(len(nums)): 
            if status < i: 
                return False 

            status = max(status, i + nums[i] )
        return True 
        