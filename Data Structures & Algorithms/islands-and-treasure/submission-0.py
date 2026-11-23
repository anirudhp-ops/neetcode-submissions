class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        
        
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque() 

        def addRoom(row, col): 

            if (row, col) not in visit: 
                if 0 <= row < ROWS and 0 <= col < COLS and grid[row][col] != -1: 
                    q.append([row, col])
                    visit.add((row, col))
        



        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 0: 
                    q.append([r, c])
                    visit.add((r, c))
        
        curr_count = 0 
        while q: 
            for i in range(len(q)): 
                r, c, = q.popleft() 

                grid[r][c] = curr_count 
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)




            
            curr_count += 1 

        





        




                
            
        

        

