class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        
        if not board:
            return board
        
        done = True
        # crush rows
        for r in range(len(board)):
            for c in range(len(board[r]) - 2):
                num1 = abs(board[r][c])
                num2 = abs(board[r][c+1])
                num3 = abs(board[r][c+2])
                
                if num1 == num2 and num2 == num3 and num1 != 0:
                    board[r][c] = num1 * -1
                    board[r][c+1] = num2 * -1
                    board[r][c+2] = num2 * -1
                    done = False
        # crush cols
        for c in range(len(board[0])):
            for r in range(len(board) - 2):
                num1 = abs(board[r][c])
                num2 = abs(board[r+1][c])
                num3 = abs(board[r+2][c])
                
                if num1 == num2 and num2 == num3 and num1 != 0:
                    board[r][c] = num1 * -1
                    board[r + 1][c] = num2 * -1
                    board[r + 2][c] = num2 * -1
                    done = False
        # gravity
        if not done:
            for c in range(len(board[0])):
                # move all positive numbers down
                idx = len(board) - 1
                for r in range(len(board) - 1, -1 , -1):
                    if board[r][c] > 0:
                        board[idx][c] = board[r][c]
                        idx -= 1
                # put zeroes in missing pieces
                for r in range(idx, -1, -1):
                    board[r][c] = 0
        
        return board if done else self.candyCrush(board)