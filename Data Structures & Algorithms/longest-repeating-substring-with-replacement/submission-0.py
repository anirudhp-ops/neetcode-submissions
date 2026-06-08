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
            print(new_s)
            print(letter)

            count = 0
            for char in new_s: 
                if char != letter:
                    count += 1
            
            if count > k: 
                first += 1 
            
            elif count <= k: 
                if second - first > result: 
                    result = second - first 
                
                second += 1 
    
        
        return result 