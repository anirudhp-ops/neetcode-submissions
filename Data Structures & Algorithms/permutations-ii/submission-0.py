class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 0: 
            return [[]]
        
        perms = self.permuteUnique(nums[1:])
        
        res = set()

        for p in perms: 
            for i in range(len(p) + 1): 
                p_val = p.copy() 
                p_val.insert(i, nums[0])
                res.add(tuple(p_val))
        
        return [list(t) for t in res]


        