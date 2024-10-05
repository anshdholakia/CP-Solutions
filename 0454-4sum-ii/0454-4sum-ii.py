class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        numscount = defaultdict(int)
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                numscount[nums3[i]+nums4[j]]+=1
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                cur_target = -(nums1[i]+nums2[j])
                count+=numscount[cur_target]
        return count
