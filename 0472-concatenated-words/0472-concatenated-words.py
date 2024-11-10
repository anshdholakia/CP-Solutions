class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words=set(words)
        memo={}
        def dfs(cur_word):
            if not cur_word:
                return 0
            if cur_word in memo:
                return memo[cur_word]
            res=-inf
            for i in range(len(cur_word)):
                if cur_word[:i+1] in words:
                    res=max(res, 1+dfs(cur_word[i+1:]))
            memo[cur_word]=res
            return res

        res=[]
        for w in words:
            if dfs(w)>1:
                res.append(w)
        return res

