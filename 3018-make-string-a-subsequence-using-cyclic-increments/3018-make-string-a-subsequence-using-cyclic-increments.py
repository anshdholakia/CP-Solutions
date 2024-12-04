class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        x, y = 0, 0
        while x<len(str1) and y<len(str2):
            if str1[x]==str2[y] or (chr(ord(str1[x])+1)==str2[y] or (str1[x]=="z" and str2[y]=="a")):
                y+=1
            x+=1
        return y==len(str2)