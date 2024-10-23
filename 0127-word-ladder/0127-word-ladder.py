class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        mapping = defaultdict(list)
        G = defaultdict(set)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                for ex in mapping[word[:i]+"*"+word[i+1:]]:
                    G[ex].add(word)
                    G[word].add(ex)
                mapping[word[:i]+"*"+word[i+1:]].append(word)
        # bfs this ting
        queue=collections.deque([(beginWord, 1)])
        visited=set({beginWord})
        while queue:
            for _ in range(len(queue)):
                pop, l = queue.popleft()
                if pop==endWord:
                    return l
                for n in G[pop]:
                    if n not in visited:
                        visited.add(n)
                        queue.append((n, l+1))
        return 0
