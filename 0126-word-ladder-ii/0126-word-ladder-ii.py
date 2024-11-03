class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        mapping = defaultdict(set)
        wordList.append(beginWord)
        for w in wordList:
            for i in range(len(w)):
                mapping[w[:i]+'*'+w[i+1:]].add(w)
        res=[]
        queue = collections.deque([beginWord])
        ladder={beginWord: []}
        while queue:
            ladder_this_lvl={}
            for _ in range(len(queue)):
                pop=queue.popleft()
                for i in range(len(pop)):
                    for n in mapping[pop[:i]+'*'+pop[i+1:]]:
                        if n==pop:
                            continue
                        if n not in ladder:
                            if n not in ladder_this_lvl:
                                ladder_this_lvl[n]=[pop]
                                queue.append(n)
                            else:
                                ladder_this_lvl[n].append(pop)
            ladder.update(ladder_this_lvl)
            if endWord in ladder:
                break
        def constructPaths(node):
            if node==beginWord:
                return [[node]]
            res=[]
            for parent in ladder.get(node,[]):
                for path in constructPaths(parent):
                    res.append(path+[node])
            return res
        construct_path = constructPaths(endWord)
        min_length=min([len(x) for x in construct_path]) if construct_path else 0
        return list(filter(lambda x: len(x)==min_length, construct_path))
