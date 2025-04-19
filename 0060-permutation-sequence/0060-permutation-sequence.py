class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        perm=list(range(1,n+1))
        res=[]
        k-=1 #(since we are indexing from 0)
        while perm:
            remaining=len(perm)-1
            fact=factorial(remaining)
            idx=k//fact
            res.append(perm[idx])
            perm.pop(idx)
            k%=fact
        return "".join(map(str,res))