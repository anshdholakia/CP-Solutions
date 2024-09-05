class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary.sort(key=lambda x: len(x))
        result = []
        for word in sentence.split(" "):
            for word2 in dictionary:
                if word.startswith(word2):
                    result.append(word2)
                    break
            else:
                result.append(word)
        return " ".join(result)