class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target=collections.Counter(s1)
        l=0
        hashmap={}
        for r in range(len(s2)):
            hashmap[s2[r]]=hashmap.get(s2[r],0)+1
            while hashmap.get(s2[r],0)>target.get(s2[r],0):
                hashmap[s2[l]]-=1
                if not hashmap[s2[l]]:
                    del hashmap[s2[l]]
                l+=1
            if hashmap==target:
                return True
        return False

