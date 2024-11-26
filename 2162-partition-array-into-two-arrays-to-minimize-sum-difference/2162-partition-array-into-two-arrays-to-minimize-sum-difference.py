# from sortedcontainers import SortedList
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # meet in the middle algo
        def get_subsets(cur_nums):
            subsets=defaultdict(list)
            subsets[0]=[0]
            for n in cur_nums:
                for k, v in deepcopy(subsets).items():
                    for s in v:
                        subsets[k+1].append(s+n)
            return subsets
        SUM=sum(nums)
        n=len(nums)//2
        MIDDLE_SUM=SUM//2
        m=(len(nums)+1)//2
        ss1, ss2 = get_subsets(nums[:m]), get_subsets(nums[m:])
        for k, v in ss2.items():
            ss2[k]=sorted(v)
        # now you basically need to go through all the possible sizes in each ss1 and find in ss2 to get the closest sum possible
        res=inf
        for k, v in ss1.items():
            for s in v:
                # do binary search on ss2[n-k]
                to_search=ss2[n-k]
                l, r = 0, len(to_search)-1
                while l<=r:
                    m=(l+r)//2
                    res=min(res, 2*abs(MIDDLE_SUM-(to_search[m]+s))+SUM%2)
                    if to_search[m]+s<MIDDLE_SUM:
                        l=m+1
                    else:
                        r=m-1
        return res