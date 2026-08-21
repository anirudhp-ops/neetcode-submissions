class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        
        people.sort()

        res = 0

        first = 0 
        second = len(people) - 1  

        while first <= second: 

            print(first)
            print(second)

            if people[first] + people[second] > limit: 

                
                second -= 1 
            

            elif people[first] + people[second] <= limit:
                first += 1 
                second -= 1 
        
            
            res += 1 
        
        print(first)
        print(second)
        
        return res 

        