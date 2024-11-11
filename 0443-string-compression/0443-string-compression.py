class Solution:
    def compress(self, chars: List[str]) -> int:
        idx=0
        cur_count=0
        cur_group=chars[0]
        i=0
        chars.append('~')
        while i<len(chars):
            if chars[i]==cur_group:
                cur_count+=1
            else:
                chars[idx]=cur_group
                if cur_count!=1:
                    for curi, d in enumerate(str(cur_count)):
                        chars[idx+curi+1]=d
                    idx+=(curi+2)
                else:
                    idx+=1
                cur_group=chars[i]
                cur_count=1
            i+=1
        return idx