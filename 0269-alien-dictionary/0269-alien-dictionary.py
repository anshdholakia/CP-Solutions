class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        print(adj)
        topo = []
        visited = set({})
        cycle = set({})
        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True
            visited.add(node)
            if not adj[node]:
                topo.append(node)
                return True
            cycle.add(node)
            for n in adj[node]:
                if not dfs(n):
                    return False
            cycle.remove(node)
            topo.append(node)
            return True
        for w in adj:
            if w not in visited and not dfs(w):
                return ""
        return "".join(topo[::-1])
            