class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rowindex=-1
        for row in matrix:
            if row[-1]>=target:
                rowindex+=1
                break
            rowindex+=1
    
        for num in matrix[rowindex]:
            if num==target:
                return True
        return False
        