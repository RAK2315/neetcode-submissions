class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top=0
        bottom=len(matrix)-1
        
        while top<=bottom:
            mid = (top+bottom)//2
            if target>matrix[mid][-1]:
                top=mid+1
            elif target < matrix[mid][0]:
                bottom=mid-1
            else:
                row=mid
                break
        else: return False
        
        for i in matrix[row]:
            # This search can be for better time complexity be binary search too
            if i == target:
                return True
        return False

