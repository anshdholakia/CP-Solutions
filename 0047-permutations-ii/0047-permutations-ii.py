class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def backtrack(cur_res, cur_choices):
            if not cur_choices:
                result.append(cur_res)
                return
            for k in range(len(cur_choices)):
                if k>0 and cur_choices[k-1]==cur_choices[k]:
                    continue
                backtrack(cur_res+[cur_choices[k]], cur_choices[:k]+cur_choices[k+1:])
        backtrack([], nums)
        return result