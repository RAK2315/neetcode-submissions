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





        """
        Better and clearner


        from collections import defaultdict

        # Each row index (0–8) maps to a set of values seen in that row
        rows = defaultdict(set)
        # Example after processing some cells:
        # rows = {
        #   0: {"5", "3", "7"},   # row 0 has seen digits 5, 3, 7
        #   1: {"6"},             # row 1 has seen digit 6
        #   2: {"1", "9", "5"}    # row 2 has seen digits 1, 9, 5
        # }

        # Each column index (0–8) maps to a set of values seen in that column
        cols = defaultdict(set)
        # Example:
        # cols = {
        #   0: {"5", "6", "8"},   # column 0 has seen digits 5, 6, 8
        #   1: {"3", "9"},        # column 1 has seen digits 3, 9
        #   4: {"7"}              # column 4 has seen digit 7
        # }

        # Each 3x3 box is identified by (row//3, col//3) and maps to a set of values seen in that box
        boxes = defaultdict(set)
        # Example:
        # boxes = {
        #   (0,0): {"5", "3", "6"},   # top-left box (rows 0–2, cols 0–2)
        #   (0,1): {"7", "9", "1"},   # top-middle box (rows 0–2, cols 3–5)
        #   (1,0): {"8"},             # middle-left box (rows 3–5, cols 0–2)
        #   (2,2): {"2", "8"}         # bottom-right box (rows 6–8, cols 6–8)
        # }

        for r in range(9):
                for c in range(9):
                    val = board[r][c]
                    if val == ".":
                        continue

                    # Check row
                    if val in rows[r]:
                        return False
                    rows[r].add(val)

                    # Check column
                    if val in cols[c]:
                        return False
                    cols[c].add(val)

                    # Check 3x3 box
                    box_index = (r // 3, c // 3)  
                    # Example: if r=4, c=7 → box_index = (1, 2)
                    # Meaning: row 4 is in the middle row block (rows 3–5 → index 1),
                    #          col 7 is in the right column block (cols 6–8 → index 2).
                    # So this cell belongs to the middle-right 3x3 box.

                    if val in boxes[box_index]:
                        return False
                    # If the digit already exists in this box’s set, Sudoku is invalid.

                    boxes[box_index].add(val)
                    # Otherwise, add the digit to the set for this box.
            return True


"""







