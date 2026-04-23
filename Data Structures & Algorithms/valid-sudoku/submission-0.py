class Solution:
    def checkRows(self, board):
        for rowIdx in range(9):
            seen = set()
            for colIdx in range(9):
                current = board[rowIdx][colIdx]
                if current == ".":
                    continue
                if current in seen:
                    return False
                seen.add(current)
        return True


    def checkCols(self, board):
        for colIdx in range(9):
            seen = set()
            for rowIdx in range(9):
                current = board[rowIdx][colIdx]
                if current == ".":
                    continue
                if current in seen:
                    return False
                seen.add(current)
        return True

    def checkSqaures(self, board):
        for squareIdx in range(9):
            seen = set()

            corner_y = (squareIdx // 3) * 3
            corner_x = (squareIdx % 3) * 3

            for colIdx in range(3):
                for rowIdx in range(3):
                    current = board[corner_y + rowIdx][corner_x +colIdx]
                    if current == ".":
                        continue
                    if current in seen:
                        return False
                    seen.add(current)
        return True



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self.checkRows(board) and 
            self.checkCols(board) and 
            self.checkSqaures(board)
            )
        
        