class Solution:
    def alienOrder(self, words: List[str]) -> str:
        G=defaultdict(set)
        for word in words:
            for w in word:
                G[w]
        for p1 in range(len(words)):
            for p2 in range(p1+1, len(words)):
                w1, w2 = words[p1], words[p2]
                i, j = 0, 0
                while i<len(w1) and j<len(w2) and w1[i]==w2[j]:
                    i+=1
                    j+=1
                if i<len(w1) and j<len(w2):
                    if w1[i] in G[w2[j]]:
                        return ""
                    G[w1[i]].add(w2[j])
                elif i<len(w1):
                    return ""
        # course schedule 2
        res=[]
        visited, cycle = set(), set()
        def dfs(letter):
            if letter in visited:
                return True
            if letter in cycle:
                return False
            cycle.add(letter)
            for neighbor in G[letter]:
                if not dfs(neighbor):
                    return False
            cycle.remove(letter)
            visited.add(letter)
            res.append(letter)
            return True
        for key in G:
            if not dfs(key):
                return ""
        return "".join(res[::-1])