class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)<len(nums2):
            nums1, nums2 = nums2, nums1
        if not nums2:
            if len(nums1)%2:
                return nums1[len(nums1)//2]
            return (nums1[len(nums1)//2]+nums1[len(nums1)//2-1])/2.0
        TOTAL = len(nums1)+len(nums2)
        HALF = TOTAL//2
        l, r = 0, len(nums2)-1
        while True:
            m = (l+r)//2
            m2 = HALF-m-1
            L2 = nums2[m] if m>=0 else -float("inf")
            R2 = nums2[m+1] if m+1<len(nums2) else float("inf")
            L1 = nums1[m2-1] if len(nums1)>m2-1>=0 else -float("inf")
            R1 = nums1[m2] if 0<=m2<len(nums1) else float("inf")
            if L2<=R1 and L1<=R2:
                if TOTAL%2:
                    return min(R1, R2)
                return (max(L1, L2)+min(R1, R2))/2.0
            if L2>R1:
                r=m-1
            else:
                l=m+1