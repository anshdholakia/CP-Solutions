class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # define the groups which can be swapped with each other
        # run through the indices and pop from queue in the groups
        groups=[]
        cur_group=collections.deque([])
        idx_to_group={}
        prev=None
        sorted_nums=sorted([(x, i) for i, x in enumerate(nums)], key=lambda x: x[0])
        for n, idx in sorted_nums:
            if prev==None:
                cur_group.append(n)
            elif n-prev<=limit:
                cur_group.append(n)
            else:
                groups.append(cur_group)
                cur_group=collections.deque([n])
            idx_to_group[idx]=len(groups)
            prev=n
        groups.append(cur_group)
        final=[]
        for i in range(len(nums)):
            final.append(groups[idx_to_group[i]].popleft())
        return final
