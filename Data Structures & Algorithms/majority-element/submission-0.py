class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int) 

        for val in nums: 
            d[val] += 1 
            if d[val] > (len(nums) / 2): 
                return val
        
        return nums[0]
        