class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        G_dummy=defaultdict(set)
        G=defaultdict(list)
        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                new_word=w[:i]+'*'+w[i+1:]
                for w1 in G_dummy[new_word]:
                    G[w1].append(w)
                    G[w].append(w1)
                G_dummy[new_word].add(w)
        # use bfs
        queue=collections.deque([beginWord])
        visited=set({beginWord})
        if beginWord==endWord:
            return 0
        res=1
        while queue:
            for _ in range(len(queue)):
                pop=queue.popleft()
                if pop==endWord:
                    return res
                for neighbor in G[pop]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            res+=1
        return 0
