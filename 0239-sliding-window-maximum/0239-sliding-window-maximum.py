class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic deque
        deque=collections.deque()
        result=[]
        for i in range(k):
            while deque and deque[-1][0]<nums[i]:
                deque.pop()
            deque.append((nums[i], i))
        result.append(deque[0][0])
        for i in range(k, len(nums)):
            while deque and deque[0][1]<=i-k:
                deque.popleft()
            while deque and deque[-1][0]<nums[i]:
                deque.pop()
            deque.append((nums[i], i))
            result.append(deque[0][0])
        return result