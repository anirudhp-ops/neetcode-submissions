class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temp) 
        for i in range(0, len(temp)): 

            if not stack: 
                stack.append(i) 

            elif stack and temp[i] <= temp[stack[-1]]: 
                stack.append(i) 

            elif stack and temp[i] > temp[stack[-1]]: 
                while stack and temp[i] > temp[stack[-1]]: 
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
            print(stack)
        
        if stack: 
            while not stack: 
                result[stack[-1]] = 0
                stack.pop() 
            

        return result 
                
            




        