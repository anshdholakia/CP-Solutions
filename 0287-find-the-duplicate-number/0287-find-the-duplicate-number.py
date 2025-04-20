class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        # find the start of the cycle
        fast=0
        while fast!=slow:
            slow=nums[slow]
            fast=nums[fast]
        return slow