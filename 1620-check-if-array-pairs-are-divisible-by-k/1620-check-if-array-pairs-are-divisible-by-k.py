class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        NEED = len(arr)//2
        mod_to_n = {}
        cur = 0
        for n in arr:
            rem = n%k
            if rem<0:
                rem+=k
            mod_to_n[rem] = mod_to_n.get(rem, 0)+1
        if mod_to_n.get(0, 0)%2:
            return False
        for i in range(1, k//2+1):
            if mod_to_n.get(i, 0) != mod_to_n.get(k-i, 0):
                return False
        return True