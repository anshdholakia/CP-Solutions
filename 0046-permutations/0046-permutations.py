class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(cur_choices, cur_list):
            if not cur_choices:
                result.append(cur_list)
                return
            for i in range(len(cur_choices)):
                backtrack(cur_choices[:i]+cur_choices[i+1:], cur_list+[cur_choices[i]])
        backtrack(nums, [])
        return result