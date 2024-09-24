class Trie:
    def __init__(self):
        self.root = {}
    def insert_word(self, word):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c]={}
            cur=cur[c]
    def find_longest(self, word):
        cur=self.root
        cur_result=0
        for c in word:
            if c not in cur:
                return cur_result
            cur=cur[c]
            cur_result+=1
        return cur_result

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))
        trie_one = Trie()
        trie_two = Trie()
        for w in arr1:
            trie_one.insert_word(w)
        result = 0
        for w in arr2:
            result=max(result, trie_one.find_longest(w))
        return result