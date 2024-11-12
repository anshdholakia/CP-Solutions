class Trie:
    def __init__(self):
        self.root={}
    def add_word(self, word):
        cur=self.root
        for w in word:
            if w not in cur:
                cur[w]={}
            cur=cur[w]
            cur['counter']=cur.get('counter',0)+1
        cur['#']=word
    def mark_word(self, word):
        cur=self.root
        for w in word:
            cur=cur[w]
            cur['counter']-=1
        del cur['#']

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie=Trie()
        for w in words:
            trie.add_word(w)
        result=[]
        visited=set({})
        def dfs(x, y, cur):
            if (x, y) in visited:
                return
            if '#' in cur[board[x][y]]:
                result.append(cur[board[x][y]]['#'])
                trie.mark_word(cur[board[x][y]]['#'])
            visited.add((x, y))
            for dx, dy in pairwise([-1,0,1,0,-1]):
                if 0<=x+dx<len(board) and 0<=y+dy<len(board[0]) and (x+dx, y+dy) not in visited and board[x+dx][y+dy] in cur[board[x][y]] and cur[board[x][y]]['counter']>0:
                    dfs(x+dx, y+dy, cur[board[x][y]])
            visited.remove((x, y))
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] in trie.root:
                    dfs(i, j, trie.root)
        return result