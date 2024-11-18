class Solution:
    def minimumDeletions(self, s: str) -> int:
        # count the number of as on the right of the index
        # cound the number of bs on the left of the index
        cur_a_count = 0
        a_count=[]
        for i in range(len(s)-1, -1, -1):
            a_count.append(cur_a_count)
            if s[i]=='a':
                cur_a_count+=1
        a_count=a_count[::-1]
        cur_b_count = 0
        b_count=[]
        for i in range(len(s)):
            b_count.append(cur_b_count)
            if s[i]=='b':
                cur_b_count+=1
        res = float("inf")
        for a, b in zip(a_count, b_count):
            res=min(res, a+b)
        return res
            
