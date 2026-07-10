from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        first = 0
        second = 1
        result = 0

        while second <= len(s): 
            new_s = s[first:second]
            trans = Counter(new_s)
            val = trans.most_common(1) ## tuple inside of list 
            letter = val[0][0]


            count = len(new_s) - val[0][1]
            
            if count > k: 
                first += 1 
            
            elif count <= k: 
                if second - first > result: 
                    result = second - first 
                
                second += 1 
    
        
        return result 