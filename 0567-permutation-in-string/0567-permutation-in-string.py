class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        target = collections.Counter(s1)
        current = {}
        for r in range(len(s2)):
            if s2[r] in target:
                current[s2[r]] = current.get(s2[r], 0) + 1
                while current[s2[r]]>target[s2[r]]:
                    if s2[l] in target:
                        current[s2[l]]-=1
                    l+=1
                if current==target:
                    return True
            else:
                l=r+1
                current={}
        return False