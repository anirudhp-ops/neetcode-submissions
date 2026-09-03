import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d = Counter(tasks)
        values = [[-v,k] for k, v in d.items()]
        print(values)

        
        heapq.heapify(values)
        print(values)
        res = 0
        queue = deque()

        while queue or values: 
            if queue and queue[0][1] <= res: 
                item = queue.popleft()
                if item[0][0] < 0:
                    heapq.heappush(values, item[0])
            
            if values:
                temp = heapq.heappop(values)
                res += 1 
                temp[0] += 1 
                if temp[0] < 0:
                    queue.append([temp, res + n])
            else:
                res += 1
        
        return res