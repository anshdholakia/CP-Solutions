class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_size = 0
        cur_size = 0
        sign = None
        for i in range(len(arr)-1):
            if arr[i+1]>arr[i]:
                if sign==True:
                    cur_size=0
                cur_size+=1
                sign=True
            elif arr[i+1]<arr[i]:
                if sign==False:
                    cur_size=0
                cur_size+=1
                sign=False
            else:
                cur_size = 0
            max_size = max(max_size, cur_size)
        return max_size+1