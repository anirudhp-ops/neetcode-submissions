class Solution:
    def trap(self, height: List[int]) -> int:
        res = []


        left_max = 0
        right_max = 0 

        for val in height: 
            if val > left_max: 
                left_max = val
                res.append(0)
                continue 
            
            elif val <= left_max: 
                cur = left_max - val 
                res.append(cur)

       

        
        for i in range(len(height) -1, -1, -1): 

            if height[i] + res[i] > right_max: 
                res[i] = right_max - height[i]
                if res[i] < 0: 
                    res[i] = 0
            
            right_max = max(right_max, height[i])

        

            
        
        return sum(res)






        
        
        