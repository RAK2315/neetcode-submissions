class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range (0,9):
            colseen=set()
            rowseen=set()
            for j in range (0,9):
                if board[i][j] in colseen and board[i][j]!=".":
                    return False
                else: colseen.add(board[i][j])

                if board[j][i] in rowseen and board[j][i]!=".":
                    return False
                else: rowseen.add(board[j][i])

        x=0
        while x<9:   
            seen1=set()
            seen2=set()
            seen3=set()
            for i in range(x,x+3):
                for j in range(0,3):
                    if board[i][j] in seen1 and board[i][j]!=".":
                        return False
                    else:seen1.add(board[i][j])

                    if board[i][j+3] in seen2 and board[i][j+3]!=".":
                        return False
                    else:seen2.add(board[i][j+3])

                    if board[i][j+6] in seen3 and board[i][j+6]!=".":
                        return False
                    else:seen3.add(board[i][j+6])
            x+=3

        return True