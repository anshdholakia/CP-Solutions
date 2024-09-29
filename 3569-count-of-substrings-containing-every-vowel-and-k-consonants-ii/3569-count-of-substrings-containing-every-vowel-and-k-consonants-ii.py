class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # prefix sums + sliding window
        c = 0
        res = 0
        v = {x:0 for x in 'aeiou'}
        ps = [len(word) for _ in range(len(word)+1)]
        for i in range(len(word)-1, -1, -1):
            if word[i] in v:
                ps[i] = ps[i+1]
            else:
                ps[i] = i
        l = 0
        for r in range(len(word)):
            if word[r] in v:
                v[word[r]]+=1
            else:
                c+=1
            while c>k:
                if word[l] in v:
                    v[word[l]]-=1
                else:
                    c-=1
                l+=1
            while c==k and min(v.values())>0:
                res += ps[r+1]-r
                if word[l] in v:
                    v[word[l]]-=1
                else:
                    c-=1
                l+=1
        return res