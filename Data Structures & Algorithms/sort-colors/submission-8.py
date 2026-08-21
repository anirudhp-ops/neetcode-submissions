"""

Understanding the Question: 

-input size
-prioritze time or space - time 

Brute Force: 
O(nlogn) - sort the array 


Optimal Solution: 
-hash map to count number of values
-0(n)

          i 
  
  0 0 1 1 0 2 2 

    F     S

  i 

0 2 1 2 1 1 2 

  F       S




Edge Cases: 
-all values in array are a single number
-empty array
-array len(1)


Code



Walk through it in the end: 

"""



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        first = 0 
        second = len(nums) - 1 

        i = 0 

        while i <= second: 
            if nums[i] == 0: 

                nums[first], nums[i] = nums[i], nums[first]
                first += 1 
                i += 1
                

            
            elif nums[i] == 2: 

                nums[second], nums[i] = nums[i], nums[second]
                second -= 1 

            else:

                i += 1 


            
        
        

        

        


