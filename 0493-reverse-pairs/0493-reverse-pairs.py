class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count=0
        def mergeSort(left_sorted, right_sorted):
            # count the number of pairs you can reverse
            left=0
            for right in range(len(right_sorted)):
                while left<len(left_sorted) and left_sorted[left]<=2*right_sorted[right]:
                    left+=1
                nonlocal count
                count+=(len(left_sorted)-left)
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
        def merge(nums):
            if len(nums)>1:
                m=len(nums)//2
                left=merge(nums[:m])
                right=merge(nums[m:])
                return mergeSort(left, right)
            return nums
        merge(nums)
        return count