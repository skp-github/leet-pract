class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row = 0
        for i in range(m):
            if target == matrix[i][-1]:
                return True
            elif target < matrix[i][-1]:
                row = i
                break
        low = 0 
        high = n-1
        while low <= high:
            mid = (low+high)//2
            if matrix[row][mid] == target:
                return True
            elif target <  matrix[row][mid]:
                high = mid-1 
            else:
                low = mid+1 
        return False 