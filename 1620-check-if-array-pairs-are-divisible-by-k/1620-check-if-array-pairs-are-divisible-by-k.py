class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        ps=defaultdict(int) # store the modulo with k
        for n in arr:
            ps[n%k]+=1
        print(ps)
        for n in ps:
            if n==0:
                if ps[n]%2!=0:
                    return False
            elif ps[k-n]!=ps[n]:
                return False
        return True