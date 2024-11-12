class Trie:
    def __init__(self):
        self.root = {}
    def add_word(self, word):
        cur=self.root
        for w in word:
            if w not in cur:
                cur[w]={}
            cur=cur[w]
        cur['#']=word
    def search_word(self, word):
        cur=self.root
        for w in word:
            if w not in cur:
                return ""
            cur=cur[w]
            if '#' in cur:
                return cur['#']
        return ""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.add_word(word)
        splitted_sentence=sentence.split(" ")
        res=[]
        for word in splitted_sentence:
            if (searched:=trie.search_word(word)):
                res.append(searched)
            else:
                res.append(word)
        return " ".join(res)