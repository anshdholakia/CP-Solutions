# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        # sort the words based on their positional uniqueness
        place_count=defaultdict(int)
        for word in words:
            for i, c in enumerate(word):
                place_count[str(i)+c]+=1
        def score_word(word):
            return sum([place_count[str(i)+c] for i, c in enumerate(word)])
        # sorted from least common to most common i.e. most unique to least unique
        words.sort(key=score_word)
        def get_diff(word1, word2):
            if word1==word2:
                return 0
            score=0
            for a, b in zip(word1, word2):
                if a==b:
                    score+=1
            return score

        end=-1
        for _ in range(30):
            chosen_word=words[end]
            score=master.guess(chosen_word)
            if score==6:
                break
            elif score==0:
                # filter out words which do not marginally match with this
                words=[word for word in words if not any(a==b for a, b in zip(word, chosen_word))]
            else:
                # the secret word would have the same number of score with the chosen_word
                words=[word for word in words if get_diff(word, chosen_word)==score]

