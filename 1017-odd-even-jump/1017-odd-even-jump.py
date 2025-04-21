from sortedcontainers import SortedList
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        sl1, sl2 = SortedList(), SortedList()
        even, odd = [0]*len(arr), [0]*len(arr)
        even[-1]=1
        odd[-1]=1
        for i in range(len(arr)-1,-1,-1):
            n=arr[i]
            idx1, idx2 = sl1.bisect_left((n, i)), sl2.bisect_left((-n, i))
            if idx1<len(sl1):
                odd[i]=even[sl1[idx1][1]]
            if idx2<len(sl2):
                even[i]=odd[sl2[idx2][1]]
            sl1.add((n, i))
            sl2.add((-n, i))
        return sum(odd)