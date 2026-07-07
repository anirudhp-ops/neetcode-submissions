class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix, postfix, result = [1] * len(nums), [1] * len(nums), [1] * len(nums)  
        
        postfix[-2] = nums[-1] 
        for i in range(len(nums) - 2, 0, -1): 
            postfix[i-1] = nums[i] * postfix[i] 
            
        
        
        prefix[1] = nums[0] 
        for i in range(1, len(nums) - 1): 
            prefix[i+1] = nums[i] * prefix[i]
            result[i] = postfix[i] * prefix[i]
        
        result[0] = postfix[0] * prefix[0]
        result[-1] = postfix[-1] * prefix[-1]

        return result 
        
        
        

 


        