class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        while l<=r:
            m=(l+r)//2
            print(l, r, m)
            if (arr[m-1] if m>0 else inf)<arr[m]>(arr[m+1] if m<len(arr)-1 else inf):
                return m
            if (arr[m-1] if m>0 else -inf)>arr[m]:
                r=m-1
            else:
                l=m+1
        
