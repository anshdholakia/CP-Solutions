class Solution:
    def alienOrder(self, words: List[str]) -> str:
        G=defaultdict(set)
        # filter the words out
        newwords=[]
        newwords.append(words[0])
        for i in range(1, len(words)):
            if words[i-1]==words[i]:
                continue
            newwords.append(words[i])
        words=newwords
        for w1 in range(len(words)):
            for c in words[w1]:
                G[c]
            for w2 in range(w1+1, len(words)):
                if (words[w2].startswith(words[w1]) or words[w1].startswith(words[w2])) and len(words[w1])>len(words[w2]):
                    return ""
                i, j = 0, 0
                while i<len(words[w1]) and j<len(words[w2]) and words[w1][i]==words[w2][j]:
                    i+=1
                    j+=1
                if i<len(words[w1]) and j<len(words[w2]):
                    G[words[w1][i]].add(words[w2][j])
        # topo sort
        visited=set({})
        cycle=set({})
        res=[]
        def dfs(letter):
            if letter in cycle:
                return False
            if letter in visited:
                return True
            cycle.add(letter)
            for neighbor in G[letter]:
                if not dfs(neighbor):
                    return False
            cycle.remove(letter)
            visited.add(letter)
            res.append(letter)
            return True
        for key in G.copy():
            if not dfs(key):
                return ""
        return "".join(res[::-1])
