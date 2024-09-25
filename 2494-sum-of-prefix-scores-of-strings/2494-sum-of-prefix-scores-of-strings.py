class Trie:
    def __init__(self):
        self.root = {}
        self.memo = {}
    def add_word(self, word, index):
        cur = self.root
        for w in word:
            if w not in cur:
                cur[w] = {'#': 0}
            cur = cur[w]
            cur['#']+=1
        cur['index'] = cur.get('index', []) + [index]

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for i, w in enumerate(words):
            trie.add_word(w, i)
        answer = [-1]*len(words)
        # traverse through the prefix tree and insert the values in answer
        def bfs(cur_dict, cur_sum):
            cur_sum += cur_dict.get('#', 0)
            for x in cur_dict:
                if x!='#' and x!='index':
                    bfs(cur_dict[x], cur_sum)
            if 'index' in cur_dict:
                for i in cur_dict['index']:
                    answer[i] = cur_sum
        bfs(trie.root, 0)
        return answer