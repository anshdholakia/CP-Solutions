class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # using binary search first find the mid point
        l, r = 0, len(arr)-1
        while l<=r:
            m=(l+r)//2
            if arr[m]==x:
                l=m-1
                r=m+1
                k-=1
                break
            elif arr[m]<x:
                l=m+1
            else:
                r=m-1
        if r<l: l,r=r,l
        # use two pointer approach to expand
        while k:
            if l==-1:
                r+=1
            elif r==len(arr):
                l-=1
            else:
                if abs(arr[l]-x)<=abs(arr[r]-x):
                    l-=1
                else:
                    r+=1
            k-=1
        return arr[l+1:r]