class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}

        for char in s: 
            if char in ("(", "[", "{"):
                
                stack.append(char)
            else:  
                if not stack: 
                    return False
                
                if stack and stack[-1] == pairs[char]:
                    stack.pop() 
                else: 
                    stack.append(char)
        
            print(stack)

        
        
        if not stack: 
            return True 
        else:
            return False   
            

        