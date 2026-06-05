class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set() 
        longest = 0; 
        for num in nums: 
            visited.add(num)
        
        curr = 0
        res = 0

        for num in nums: 
            val = num
            
            while val in visited: 
                val += 1 
                res += 1 
            
            if res > curr:
                curr = res 
            res = 0 


        return curr  
                    
                