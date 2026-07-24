class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        

        def dfs(numbers): 
           
            if sum(subset) == target and subset not in res: 
                res.append(subset.copy()) 
            
            if sum(subset) > target: 
                return 

            if not numbers: 
                return 
            
            else: 
                subset.append(numbers[0])
                dfs(numbers)

                subset.pop()
                dfs(numbers[1:])

            
        dfs(nums) 
        return res