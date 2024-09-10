class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set({})
        def backtrack(i, j, cur_word):
            if not cur_word:
                return True
            if (i, j) in visited:
                return False
            if i<0 or i>=len(board) or j<0 or j>=len(board[0]):
                return False
            if board[i][j]!=cur_word[0]:
                return False
            visited.add((i, j))
            result = backtrack(i+1, j, cur_word[1:]) or backtrack(i, j+1, cur_word[1:]) or backtrack(i, j-1, cur_word[1:]) or backtrack(i-1, j, cur_word[1:])
            visited.remove((i, j))
            return result
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0] and backtrack(i, j, word):
                    return True
        return False