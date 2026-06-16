class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top < bottom:
            mid = top + (bottom - top) // 2

            if matrix[mid][0] > target:
                bottom = mid
            else:
                top = mid + 1

        row = top - 1 if top > 0 and matrix[top][0] > target else top

        left = 0
        right = len(matrix[0]) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False