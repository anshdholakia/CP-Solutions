class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # maximize when its player 1s chance and minimize
        @cache
        def chance(player_one, l, r):
            if l>r:
                return 0
            if player_one:
                # you have two choices, either take first or last elem
                return max(nums[l]+chance(False, l+1, r),nums[r]+chance(False, l, r-1))
            else:
                # you have two choices either take first or last elem
                return min(-nums[l]+chance(True, l+1, r), -nums[r]+chance(True, l, r-1))
        return chance(True, 0, len(nums)-1)>=0