class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid: 
            return 0 

        res = 0 
        
        rows = len(grid) 
        cols = len(grid[0])

        visited = set() 
        

        def dfs(row, col): 


            if grid[row][col] != 1: 
                return 0


            else: 
                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                area = 1 

                for dr, dc in directions: 
                    r = row + dr 
                    c = col + dc 
                
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == 1: 

                        visited.add((r, c)) 

                        area += dfs(r, c) 
                    
                return area 




                

        



        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1 and (r,c) not in visited: 
                    visited.add((r,c))
                    
                    area = dfs(r,c)
                    res = max(area, res)
        

        return res 

        