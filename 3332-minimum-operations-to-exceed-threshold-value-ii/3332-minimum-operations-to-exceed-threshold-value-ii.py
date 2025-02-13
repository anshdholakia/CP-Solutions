class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        op=0
        while len(nums)>=2 and nums[0]<k:
            op+=1
            nums1, nums2 = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, min(nums1, nums2)*2+max(nums1, nums2))
        return op