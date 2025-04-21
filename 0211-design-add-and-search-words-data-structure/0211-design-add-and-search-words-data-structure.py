class WordDictionary:

    def __init__(self):
        self.map={}        

    def addWord(self, word: str) -> None:
        cur_map=self.map
        for w in word:
            if w not in cur_map:
                cur_map[w]={}
            cur_map=cur_map[w]
        cur_map['#']=True

    def search(self, word: str, cur_map='Init') -> bool:
        if cur_map=='Init':
            cur_map=self.map
        if not word:
            return cur_map.get('#',False)
        if word[0]!='.':
            return self.search(word[1:], cur_map[word[0]]) if word[0] in cur_map else False
        res=False
        for k, v in cur_map.items():
            if k!='#':
                res=res or self.search(word[1:], v)
            if res:
                break
        return res


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)