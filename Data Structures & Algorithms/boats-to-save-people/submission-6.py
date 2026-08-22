class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        res = 0

        start = 1
        end = limit 
    

        count = [0] * (limit + 1)

        for weight in people: 
            count[weight] += 1 

        print(count)

        while start <= end: 
            if start == end and count[start] == 1:
                res += 1 
                break 
            if count[start] == 0: 
                start += 1 
                continue 
            elif count[end] == 0:
                end -= 1 
                continue 
            
            elif start + end > limit: 
                count[end] -= 1 
                res += 1 
            
            elif start + end <= limit: 
                count[end] -= 1 
                count[start] -= 1 
                res += 1 
            
        
        return res 
            
            
        

      


        

        