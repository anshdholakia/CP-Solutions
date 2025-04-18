# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        while True:
            word=random.choice(words)
            guess=master.guess(word)
            new_words=[]
            if guess==0:
                # remove all words which match with this word
                for w in words:
                    for i, c in enumerate(w):
                        if c==word[i]:
                            break
                    else:
                        new_words.append(w)
            elif guess==6:
                return
            else:
                for w in words:
                    cnt=0
                    for i, c in enumerate(w):
                        if c==word[i]:
                            cnt+=1
                    if cnt==guess:
                        new_words.append(w)
            words=new_words