class Solution:
    @cache
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        if s[0]=='0':
            return 0
        if len(s)>1 and 10<=int(s[:2])<=26:
            return self.numDecodings(s[1:])+self.numDecodings(s[2:])
        return self.numDecodings(s[1:])