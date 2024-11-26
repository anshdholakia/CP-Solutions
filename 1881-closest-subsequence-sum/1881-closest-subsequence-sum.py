class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def sorted_sums(cur_nums):
            sums=set({0})
            for n in cur_nums:
                for s in sums.copy():
                    sums.add(n+s)
            return sorted(list(sums))
        m=(len(nums)//2)
        num1, num2 = sorted_sums(nums[:m]), sorted_sums(nums[m:])
        i, j = 0, len(num2)-1
        res=inf
        while i<len(num1) and j>=0:
            SUM=num1[i]+num2[j]
            res=min(res, abs(goal-SUM))
            if SUM>goal:
                j-=1
            else:
                i+=1
        return res