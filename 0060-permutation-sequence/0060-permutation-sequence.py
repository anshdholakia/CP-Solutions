class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # brute force -> get all perms till k
        cur_perm=list(range(1,n+1))
        for _ in range(k-1):
            # get next_perm
            break_idx=None
            for i in range(len(cur_perm)-1, -1, -1):
                if i>0 and cur_perm[i-1]<cur_perm[i]:
                    break_idx=i
                    break
            if break_idx==None:
                cur_perm=cur_perm[::-1]
                continue
            # get the smallest but larger than cur_perm[break_idx-1]
            small_idx=i
            for k in range(len(cur_perm)-1, i, -1):
                if cur_perm[i-1]<cur_perm[k]:
                    small_idx=k
                    break
            cur_perm[i-1], cur_perm[small_idx] = cur_perm[small_idx], cur_perm[i-1]
            l, r = i, len(cur_perm)-1
            while l<r:
                cur_perm[l], cur_perm[r] = cur_perm[r], cur_perm[l]
                r-=1
                l+=1
        return "".join(map(str,cur_perm))