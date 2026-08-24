class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        curr_s = '' 
        count = 0  
        
        for char in s: 
            if not stack: 
                stack.append([char, 1])
                
            
            else: 
                if char == stack[-1][0]: 
                    
                    curr_count = stack[-1][1] 
                    stack.append([char, curr_count + 1]) 

                    
                    if stack[-1][1] == k: 
                        stack = stack[:-k]

                        
                
                else: 
                    stack.append([char, 1])
                    
        res = ''
        for char, i in stack: 
            res += char

        
        return res
                

        