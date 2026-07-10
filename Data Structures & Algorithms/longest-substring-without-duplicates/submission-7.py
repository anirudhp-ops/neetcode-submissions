class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1: 
            return 1 
        left = 0
        right = 1
        result = 0
        while right < len(s): 
            new_s = s[left:right] 
            if s[right] not in new_s: 
                right += 1 
                if len(s[left: right  ]) > result: 
                    result = len(s[left: right ])
            elif s[right] in new_s: 
                left += 1 
        return result 

            
        

        

        