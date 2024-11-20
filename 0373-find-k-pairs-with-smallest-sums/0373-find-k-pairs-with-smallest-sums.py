class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result=[]
        minheap=[(nums1[0]+nums2[0], 0, 0)]
        for _ in range(k):
            _, i, j = heapq.heappop(minheap)
            result.append([nums1[i], nums2[j]])
            if i+1<len(nums1):
                heapq.heappush(minheap, (nums1[i+1]+nums2[j], i+1, j))
            if i==0 and j+1<len(nums2):
                heapq.heappush(minheap, (nums1[i]+nums2[j+1], i, j+1))
        return result