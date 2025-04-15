class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums2:
            nums1, nums2 = nums2, nums1
        if not nums1:
            if len(nums2)%2==0:
                return (nums2[len(nums2)//2]+nums2[(len(nums2)//2)-1])/2
            return nums2[len(nums2)//2]
        if len(nums1)<len(nums2):
            nums1, nums2 = nums2, nums1
        l, r = 0, len(nums2)-1
        total=len(nums1)+len(nums2)
        half=total//2
        while True:
            m=(l+r)//2
            L2=nums2[m] if 0<=m<len(nums2) else -inf
            R2=nums2[m+1] if 0<=m+1<len(nums2) else inf
            L1=nums1[half-m-2] if 0<=half-m-2<len(nums1) else -inf
            R1=nums1[half-m-1] if 0<=half-m-1<len(nums1) else inf
            if L2<=R1 and L1<=R2:
                if total%2==0:
                    return (max(L1, L2)+min(R1, R2))/2
                return min(R1, R2)
            if L2>R1:
                r=m-1
            else:
                l=m+1
