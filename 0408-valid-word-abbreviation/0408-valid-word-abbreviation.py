class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        splitted_abbr = []
        digit = ""
        for i in range(len(abbr)):
            if abbr[i] in '1234567890':
                digit+=abbr[i]
            else:
                if digit:
                    if digit[0]=='0':
                        return False
                    splitted_abbr.append(int(digit))
                splitted_abbr.append(abbr[i])
                digit=""
        if digit:
            if digit[0]=='0':
                return False
            splitted_abbr.append(int(digit))
        i = 0
        for n in splitted_abbr:
            if i>=len(word):
                return False
            if isinstance(n, int):
                i+=n
            else:
                if word[i]!=n:
                    return False
                i+=1
        return i==len(word)
                