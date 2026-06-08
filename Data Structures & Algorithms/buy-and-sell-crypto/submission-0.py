class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        result = 0
        first = 0
        smallest_first = 101
        second = 1 
        
        while second < len(prices): 

            if prices[first] < smallest_first: 
                smallest_first = prices[first]
                
            
            val = prices[second] - smallest_first 
            

            if val > result: 
                result = val 
            
            second += 1 
            first += 1 
            
        
        
        if result < 0: 
            return 0
        return result 
            
        

        