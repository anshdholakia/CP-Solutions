from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl=SortedList()
        res=[]
        for n in reversed(nums):
            res.append(sl.bisect_left(n))
            sl.add(n)
        return res[::-1]