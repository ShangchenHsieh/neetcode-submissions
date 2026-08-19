class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rol = defaultdict(set)
        col = defaultdict(set)
        squa = defaultdict(set)

        for r in range(len(board)): 
            for c in range(len(board[0])): 
                
                if board[r][c] == '.': # the skip condition
                    continue 

                if (board[r][c] in rol[r] or 
                board[r][c] in col[c] or 
                board[r][c] in squa[(r//3, c//3)]): 
                    return False 

                rol[r].add(board[r][c])
                col[c].add(board[r][c])
                squa[(r//3, c//3)].add(board[r][c])

        return True