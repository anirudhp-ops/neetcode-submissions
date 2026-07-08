class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = []
        for i in range(0, len(matrix)): 
            self.mat.append([])
            self.mat[i].append(matrix[i][0])
            for j in range(1, len(matrix[i])):
                val = self.mat[i][j - 1] + matrix[i][j]
                self.mat[i].append(val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        result = 0

        if len(self.mat) == 1 and len(self.mat[0]) == 1:
            return self.mat[0][0]
        for i in range(row1, row2 + 1): 
            if col1 > 0: 
                result += (self.mat[i][col2] - self.mat[i][col1 - 1]) 
            else: 
                result += self.mat[i][col2]

            
        
        return result 


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)