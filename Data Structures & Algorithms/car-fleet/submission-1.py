from collections import defaultdict

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        result = 1

        dic = defaultdict(int) 

        for i in range(0, len(position)): 
            dic[position[i]] = speed[i] 
        
        sorted_d = dict(sorted(dic.items(), key=lambda x: x[0], reverse=True))  # fix 1: sort by position

        for val in sorted_d: 
            time = (target - val) / sorted_d[val]  # use float division
            if not stack: 
                stack.append(time)
            elif time > stack[-1]:  # fix 2: new fleet only if slower
                stack.append(time)
        
        return len(stack)
