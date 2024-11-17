class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        deque=collections.deque([])
        cur_sum=0
        res=inf
        for r in range(len(nums)):
            cur_sum+=nums[r]
            if cur_sum>=k:
                res=min(res, r+1)
            while deque and cur_sum-deque[0][0]>=k:
                res=min(res, r-deque[0][1])
                deque.popleft()
            while deque and deque[-1][0]>cur_sum:
                deque.pop()
            deque.append((cur_sum, r))
        return res if res!=inf else -1