class Solution:
    def countAndSay(self, n: int) -> str:
        cur_str="1"
        for _ in range(n-1):
            new_str=""
            idx=1
            count=1
            cur_digit=cur_str[0]
            while idx<len(cur_str):
                if cur_str[idx]==cur_digit:
                    count+=1
                else:
                    new_str+=(str(count)+cur_digit)
                    cur_digit=cur_str[idx]
                    count=1
                idx+=1
            new_str+=(str(count)+cur_digit)
            cur_str=new_str
        return cur_str