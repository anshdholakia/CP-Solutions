class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        # now find the start of the cycle
        slow1, slow2 = slow, nums[0]
        while slow1!=slow2:
            slow1=nums[slow1]
            slow2=nums[slow2]
        return slow1