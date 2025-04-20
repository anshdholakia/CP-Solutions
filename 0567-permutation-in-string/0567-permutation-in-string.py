class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count={}
        target=collections.Counter(s1)
        l=0
        have=0
        for r in range(len(s2)):
            if s2[r] not in target:
                count={}
                l=r+1
                have=0
                continue
            count[s2[r]]=count.get(s2[r],0)+1
            have+=1
            while count[s2[r]]>target[s2[r]]:
                count[s2[l]]-=1
                l+=1
                have-=1
            if have==len(s1):
                return True
        return False