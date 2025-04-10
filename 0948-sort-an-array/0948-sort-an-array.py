class Solution:
    def merge(self, A, B):
        C=[]
        i, j = 0, 0
        while i<len(A) and j<len(B):
            if A[i]<B[j]:
                C.append(A[i])
                i+=1
            else:
                C.append(B[j])
                j+=1
        return C+A[i:]+B[j:]
    def mergeSort(self, nums):
        if len(nums)>1:
            m=len(nums)//2
            A=self.mergeSort(nums[:m])
            B=self.mergeSort(nums[m:])
            return self.merge(A, B)
        return nums
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)