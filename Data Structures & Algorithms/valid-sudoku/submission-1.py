class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dic = defaultdict(set)
        col_dic = defaultdict(set)
        box_dic = defaultdict(set)

        for c in range(9): 
            for r in range(9): 
                if board[r][c] == '.': 
                    continue 
                elif (board[r][c] in row_dic[r] or 
                board[r][c] in col_dic[c] or 
                board[r][c] in box_dic[(r//3, c//3)]):
                    return False 
                row_dic[r].add(board[r][c])
                col_dic[c].add(board[r][c])
                box_dic[(r//3, c//3)].add(board[r][c])

        return True