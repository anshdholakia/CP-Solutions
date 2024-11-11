class TicTacToe:

    def __init__(self, n: int):
        self.board=[['.' for _ in range(n)] for _ in range(n)]

    def move(self, row: int, col: int, player: int) -> int:
        origr=row
        if player==1:
            self.board[row][col]='X'
            letter='X'
        else:
            self.board[row][col]='O'
            letter='O'
        if row==col:
            # check left diagonal \
            left1, left2= 0, 0
            origr=row
            row-=1
            while row>=0 and self.board[row][row]==letter:
                left1+=1
                row-=1
            row=origr
            row+=1
            while row<len(self.board) and self.board[row][row]==letter:
                left2+=1
                row+=1
            if left1+left2+1==len(self.board):
                return player
        row=origr
        if row==len(self.board)-col-1:
            # check right diagonal /
            right1, right2 = 0, 0
            origr=row
            row-=1
            while 0<=row<len(self.board) and self.board[row][len(self.board)-row-1]==letter:
                right1+=1
                row-=1
            row=origr
            row+=1
            while 0<=row<len(self.board) and self.board[row][len(self.board)-row-1]==letter:
                right2+=1
                row+=1
            if right1+right2+1==len(self.board):
                return player
        # check horizontal _
        count=0
        for i in range(len(self.board)):
            if self.board[i][col]==letter:
                count+=1
        if count==len(self.board):
            return player

        # check vertical |
        count=0
        for i in range(len(self.board)):
            if self.board[origr][i]==letter:
                count+=1
        if count==len(self.board):
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)