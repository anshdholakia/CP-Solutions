class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq, maxq = deque([]), deque([])
        l=0
        res=-inf
        for r in range(len(nums)):
            # insert in minq
            while minq and minq[-1]>nums[r]:
                minq.pop()
            minq.append(nums[r])
            # insert in maxq
            while maxq and maxq[-1]<nums[r]:
                maxq.pop()
            maxq.append(nums[r])
            while maxq[0]-minq[0]>limit:
                if nums[l]==minq[0]:
                    minq.popleft()
                elif nums[l]==maxq[0]:
                    maxq.popleft()
                l+=1
            res=max(res, r-l+1)
        return res