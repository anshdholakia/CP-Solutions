class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        l, r = 0, min(len(tasks), len(workers))
        ans=0
        def check(k):
            if k==0:
                return True
            if k>len(workers): return False
            count=Counter(workers[-k:])
            sorted_keys=sorted(count.keys())
            used_pill=0
            for i in range(k-1, -1, -1):
                if sorted_keys[-1]>=tasks[i]:
                    count[sorted_keys[-1]]-=1
                    if not count[sorted_keys[-1]]: 
                        del count[sorted_keys[-1]]
                        sorted_keys.pop()
                elif used_pill<pills:
                    required = tasks[i]-strength
                    l, r = 0, len(sorted_keys)-1
                    idx=-1
                    while l<=r:
                        m=(l+r)//2
                        if sorted_keys[m]<required:
                            l=m+1
                        else:
                            idx=m
                            r=m-1
                    if idx==-1: return False
                    count[sorted_keys[idx]]-=1
                    if not count[sorted_keys[idx]]: 
                        del count[sorted_keys[idx]]
                        sorted_keys.pop(idx)
                    used_pill+=1
                else:
                    return False
            return True
        while l<=r:
            m=(l+r)//2
            if check(m):
                ans=m
                l=m+1
            else:
                r=m-1
        return ans