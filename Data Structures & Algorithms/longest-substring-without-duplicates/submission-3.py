class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        left = 0
        right = 1 

        new_s = s[left:right]; 
        result = 1; 

        while right < len(s): 

            new_s = s[left:right]

            if s[right] not in new_s: 
                
                right += 1 

                if right - left > result: 
                    result = right - left
                
            

            elif s[right]  in new_s: 
               

                left += new_s.index(s[right]) + 1
                right += 1 
            
        
        return result 


        