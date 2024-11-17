class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # use merge and divide and for each of the sorted arrays
        # do a sliding window to check how many ranged can be fitted here
        ps=[]
        curs=0
        for n in nums:
            curs+=n
            ps.append(curs)
        count=0
        for n in ps:
            if lower<=n<=upper:
                count+=1
        def merge(left_sorted, right_sorted):
            # use sliding window to get the possible ranges
            l=0
            r=0
            for idx in range(len(left_sorted)):
                while l<len(right_sorted) and right_sorted[l]-left_sorted[idx]<lower:
                    l+=1
                while r<len(right_sorted) and right_sorted[r]-left_sorted[idx]<=upper:
                    r+=1
                nonlocal count
                count+=(r-l)
            sorted_arr=[]
            i, j = 0, 0
            while i<len(left_sorted) and j<len(right_sorted):
                if left_sorted[i]<right_sorted[j]:
                    sorted_arr.append(left_sorted[i])
                    i+=1
                else:
                    sorted_arr.append(right_sorted[j])
                    j+=1
            return sorted_arr+left_sorted[i:]+right_sorted[j:]

        def mergeSort(nums):
            if len(nums)>1:
                m=len(nums)//2
                left=mergeSort(nums[:m])
                right=mergeSort(nums[m:])
                return merge(left, right)
            return nums

        mergeSort(ps)
        return count