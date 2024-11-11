class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=list(map(int, version1.split(".")))
        version2=list(map(int, version2.split(".")))
        # remove trailing zeros
        while version1 and version1[-1]==0:
            version1.pop()
        while version2 and version2[-1]==0:
            version2.pop()
        i, j = 0, 0
        while i<len(version1) and j<len(version2):
            if version1[i]==version2[j]:
                i+=1
                j+=1
                continue
            if version1[i]>version2[j]:
                return 1
            else:
                return -1
        if i==len(version1) and j==len(version2):
            return 0
        if i<len(version1):
            return 1
        return -1