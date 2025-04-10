class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # use quickselect
        def quickselect(one_color, two_color):
            l, r = 0, len(nums)-1
            while l<r:
                while l<r and nums[l]!=one_color:
                    l+=1
                while r>l and nums[r]!=two_color:
                    r-=1
                if l<r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l+=1
                    r-=1
        quickselect(2, 0)
        quickselect(1, 0)
        quickselect(2, 1)