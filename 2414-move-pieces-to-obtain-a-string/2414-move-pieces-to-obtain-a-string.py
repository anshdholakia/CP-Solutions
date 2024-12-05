class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # s you are going through the target
        # keep track of how many rs you encountered
        # if the count of rs in target exceeds, return false
        # if the count of ls in start exceeds, return false
        if start.replace("_", "")!=target.replace("_",""):
            return False
        start_l, start_r = 0, 0
        target_l, target_r = 0, 0
        for i, j in zip(start, target):
            if i=='L':
                start_l+=1
            elif i=='R':
                start_r+=1
            if j=='L':
                target_l+=1
            elif j=='R':
                target_r+=1
            if target_r>start_r:
                return False
            if start_l>target_l:
                return False
        return True