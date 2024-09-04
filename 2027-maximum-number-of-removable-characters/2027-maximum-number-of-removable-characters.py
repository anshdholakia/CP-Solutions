class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        result = 0
        def check_subsequence(new_s, new_p, removed):
            i1, i2 = 0, 0
            while i1<len(new_s) and i2<len(new_p):
                if i1 not in removed and new_s[i1]==new_p[i2]:
                    i2+=1
                i1+=1
            return i2==len(new_p)
        # do this in binary search since you can have the removal subarray as a set and check if you can still have a subsequence even after removing all those characters
        l, r = 0, len(removable)-1
        res = 0
        while l<=r:
            m = (l+r)//2
            if check_subsequence(s, p, set(removable[:m+1])):
                res = max(res, m+1)
                l=m+1
            else:
                r=m-1
        return res

