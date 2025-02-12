class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_val=-1
        set_n={}
        for n in nums:
            new_n=0
            cur_n=n
            while cur_n:
                new_n+=cur_n%10
                cur_n//=10
            if new_n in set_n:
                max_val=max(max_val, n+set_n[new_n])
            set_n[new_n]=max(set_n.get(new_n,-inf),n)
        return max_val