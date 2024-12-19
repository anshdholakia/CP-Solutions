class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = list(range(len(arr)))
        visited, sorted_visited=set({}), set({})
        res=0
        for i, n in enumerate(arr):
            visited.add(n)
            sorted_visited.add(sorted_arr[i])
            if not visited-sorted_visited:
                res+=1
        return res

        
