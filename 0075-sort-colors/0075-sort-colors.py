class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # quick select algorithm
        def quick_select(i, j, swp1, swp2):
            while i<j:
                while i<j and nums[i]!=swp2:
                    i+=1
                while i<j and nums[j]!=swp1:
                    j-=1
                if i<j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1
                    j-=1
        quick_select(0, len(nums)-1, 0, 2)
        quick_select(0, len(nums)-1, 0, 1)
        quick_select(0, len(nums)-1, 1, 2)
        
            