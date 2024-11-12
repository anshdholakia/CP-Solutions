class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends=set(deadends)
        queue = collections.deque(["0000"])
        visited=set({"0000"})
        changes=-1
        while queue:
            changes+=1
            for _ in range(len(queue)):
                formation=queue.popleft()
                if formation==target:
                    return changes
                if formation in deadends:
                    continue
                for i in range(4):
                    for dx in [-1,1]:
                        newformation=formation[:i]+str((int(formation[i])+dx)%10)+formation[i+1:]
                        if newformation not in deadends and newformation not in visited:
                            visited.add(newformation)
                            queue.append(newformation)
        return -1
        
