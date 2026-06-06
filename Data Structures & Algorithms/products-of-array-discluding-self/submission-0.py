class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = [1] * n
    

        
        store = 1 
 
        for i in range(0, len(nums) - 1 ):
            store = store * nums[i]
            res[i + 1] = store 
        store = 1 
        
        for i in range(len(nums) - 1, 0, -1):
            store = store * nums[i] 
            res[i-1] = res[i-1] * store
        

        return res


        