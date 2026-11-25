class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLS = len(heights), len(heights[0])
        Pacific_edges = []
        Atlantic_edges = []

        for i in range(COLS): 
            Pacific_edges.append((0, i))
        
        for i in range(1, ROWS): 
            Pacific_edges.append((i, 0))

        
        for i in range(ROWS): 
            Atlantic_edges.append((i, COLS - 1))
        
        for i in range(COLS): 
            Atlantic_edges.append((ROWS - 1, i))
        
        
        def bfs(starts): 
            q = deque(starts)
            visit = set(starts) 

            while q: 
                row, col = q.popleft() 

                coordinates = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]

                for r, c in coordinates: 
                    if 0 <= r < ROWS and 0 <= c < COLS: 
                        if (r, c) not in visit and heights[r][c] >= heights[row][col] : 
                            visit.add((r, c))
                            q.append([r, c])
            
        
            return visit 
        
        pacific_flow = bfs(Pacific_edges)

        atlantic_flow = bfs(Atlantic_edges)

        return [list(cell) for cell in pacific_flow & atlantic_flow]






        

