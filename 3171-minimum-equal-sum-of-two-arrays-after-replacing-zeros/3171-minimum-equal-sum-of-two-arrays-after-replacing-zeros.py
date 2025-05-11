class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        zero1, zero2 = nums1.count(0), nums2.count(0)
        l, r = max(sum1, sum2), sum1+sum2+zero1+zero2
        print(sum1, sum2)
        if not zero1 and sum1<sum2+zero2: return -1
        elif not zero2 and sum2<sum1+zero1: return -1
        ans=-1
        def check(k):
            return k-sum1-zero1>=0 and k-sum2-zero2>=0
        while l<=r:
            m=(l+r)//2
            if check(m):
                ans=m
                r=m-1
            else:
                l=m+1
        return ans
