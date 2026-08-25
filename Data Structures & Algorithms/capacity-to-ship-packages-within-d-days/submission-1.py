"""

Inital solution: 
- compute all possible subarray, 
-O(D^n)

Optimal Solution: 
- prefix sums 

- binary search array 
    -search from max value in array to sum of all weights 
    -find the mid point 

    10 - 26 
    18 
    10-18
    14
    10 - 14
    10 - 12 
    10 - 11 

    []

    because only 2 days - we can reduce the weight 


Edge Cases: 
- empty weights 
- all the same weight 
- 



"""

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        res = 0 
        
        low = max(weights) 
        high = sum(weights) 

        # 15 
        # 5 
       

        while low < high: 
            
            mid = low + (high - low) // 2 

            count = 1 
            curr = 0

            for val in weights: 
                
                curr += val 
                if curr > mid: 
                    curr = val 
                    count += 1 

            print(mid )
            print(count)
            if count > days:
                low = mid + 1 
            
            if count < days: 
                print("hello")
                high = mid - 1 

            if count <= days: 
                res = mid 
                high = mid
        

        if res == 0: 
            res = sum(weights)
        return res 

            












        