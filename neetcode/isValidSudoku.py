leetcode_submission_link = f'https://leetcode.com/problems/valid-sudoku/submissions/1132301231'

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(
            set
        )  # key = (r/3, c/3) for checking smaller boxes

        for r in range(9):
            for c in range(9):
                # check if value is empty
                if board[r][c] == ".":
                    continue

                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                    # already seens the the value

                # normally update value
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
