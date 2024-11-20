class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # find the maximum subarray here with the count of each character less han total-k
        if k==0:
            return 0
        cur_count={'a':0, 'b':0, 'c':0}
        total=collections.Counter(s)
        l=0
        max_subarray=-1
        for r in range(len(s)):
            cur_count[s[r]]+=1
            while l<=r and cur_count[s[r]]>total[s[r]]-k:
                cur_count[s[l]]-=1
                l+=1
            max_subarray=max(max_subarray, r-l+1)
        result=-1
        if len(total)==3 and min(total.values())>=k:
            result=len(s)
            if max_subarray!=-1:
                result=len(s)-max_subarray
        return result

