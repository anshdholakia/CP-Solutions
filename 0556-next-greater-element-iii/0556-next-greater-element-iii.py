class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # return the next possible permutation
        n=list(str(n))
        max_elem=len(n)-1
        for i in range(len(n)-2,-1,-1):
            if n[i]<n[max_elem]:
                break
            if n[max_elem]<=n[i]:
                max_elem=i
        if max_elem==0:
            return -1
        # find the closest swappable in right portion
        pvt=max_elem
        for k in range(pvt, len(n)):
            if n[i]<n[k]<n[pvt]:
                pvt=k
        # swap pvt and i now
        n[i], n[pvt]=n[pvt], n[i]
        # sort all the remaining elements after i
        for k, d in enumerate(sorted(n[i+1:])):
            n[i+k+1]=d
        res= int("".join(n))
        return res if res<(1<<32-1) else -1

