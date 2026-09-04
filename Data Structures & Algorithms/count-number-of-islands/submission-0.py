class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid: 
            return 0

        res = 0 

        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            while queue: 
                r, c = queue.popleft() 
                for dr, dc in directions: 
                    dx = r + dr 
                    dy = c + dc 
                    if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == "1" and (dx,dy) not in visited: 
                        queue.append((dx, dy))
                        visited.add((dx,dy))
                

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == "1" and (r,c) not in visited: 
                    
                    visited.add((r,c))
                    bfs(r, c)
                    res += 1 

        return res  
                

        
        