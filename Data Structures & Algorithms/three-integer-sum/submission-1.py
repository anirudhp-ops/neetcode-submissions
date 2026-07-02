class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() ## n log n 
        result = []
        

        
        for i in range(0, len(nums)): 

            left = i + 1 
            right = len(nums) - 1 
            print("hello")
            while left < right: 
                
                if nums[i] + nums[left] + nums[right] == 0:
                    if [nums[i], nums[left], nums[right]] not in result: 
                        result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                
                else:
                    right -= 1 
        
        return result 


