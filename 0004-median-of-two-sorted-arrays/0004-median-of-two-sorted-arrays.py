class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # use binary search
        if not nums1 or not nums2:
            nums1+=nums2
            if len(nums1)%2:
                return nums1[len(nums1)//2]
            return (nums1[len(nums1)//2]+nums1[(len(nums1)//2)-1])/2
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        TOTAL=len(nums1)+len(nums2)
        HALF=TOTAL//2
        l, r = 0, len(nums1)-1
        while True:
            m=(l+r)//2
            LOWER1, UPPER1 = nums1[m] if 0<=m<len(nums1) else -inf, nums1[m+1] if 0<=m+1<len(nums1) else inf
            LOWER2, UPPER2 = nums2[HALF-m-2] if 0<=HALF-m-2<len(nums2) else -inf, nums2[HALF-m-1] if 0<=HALF-m-1<len(nums2) else inf
            if LOWER1<=UPPER2 and LOWER2<=UPPER1:
                if TOTAL%2:
                    return min(UPPER1, UPPER2)
                return (min(UPPER1, UPPER2)+max(LOWER1, LOWER2))/2
            if LOWER1>UPPER2:
                r=m-1
            else:
                l=m+1
