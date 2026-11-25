class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        q = deque()
        visit = set()

        def changefruit(row, col): 
            if 0 <= row < ROWS and 0 <= col < COLS:
                if (row, col) not in visit and grid[row][col] == 1: 

                    visit.add((row, col))
                    grid[row][col] = 2 
                    q.append([row, col])
        

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 2: 
                    visit.add((r, c))
                    q.append([r, c]) 
        
        minute_counter = 0
       
        while q: 
            for i in range(len(q)): 
                curr_row, curr_col = q.popleft() 
                
                changefruit(curr_row - 1, curr_col )
                changefruit(curr_row + 1, curr_col )
                changefruit(curr_row, curr_col - 1 )
                changefruit(curr_row, curr_col + 1 )

            if q: 
                minute_counter += 1 


         

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 1: 
                    return -1
                    
        

        return minute_counter


        

    
                
            




        