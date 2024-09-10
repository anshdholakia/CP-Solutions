class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie
        for w in word:
            cur[w]=cur.get(w, {})
            cur=cur[w]
        cur["#"]=True

    def search(self, word: str, cur=None) -> bool:
        cur = self.trie if not cur else cur
        for i in range(len(word)):
            if word[i]!='.':
                if word[i] not in cur:
                    return False
                cur = cur[word[i]]
            else:
                return any([self.search(word[i+1:], cur[k]) for k in cur if k!='#'])
        return cur.get("#", False)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)