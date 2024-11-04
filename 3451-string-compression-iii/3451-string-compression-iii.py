class Solution:
    def compressedString(self, word: str) -> str:
        comp=""
        cur_count=0
        prev_c=""
        if not word:
            return ""
        for i, c in enumerate(word):
            if (prev_c and c!=prev_c) or cur_count==9:
                comp+=f'{cur_count}{prev_c}'
                cur_count=0
            cur_count+=1
            prev_c=c
        comp+=f'{cur_count}{prev_c}'
        return comp