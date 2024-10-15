class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        tot = 0
        l = 0
        for r in range(len(arr)):
            if r-l+1>k:
                tot-=arr[l]
                l+=1
            tot+=arr[r] 
            if r-l+1==k and tot/k>=threshold:
                result+=1
        return result