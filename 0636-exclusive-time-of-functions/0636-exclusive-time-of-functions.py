class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive=[0]*n
        latest_time=0
        stack=[]
        for l in logs:
            l=l.split(":")
            if l[1]=="start":
                if stack:
                    exclusive[stack[-1][0]]+=(int(l[2])-latest_time)
                stack.append((int(l[0]), int(l[2])))
                latest_time=int(l[2])
            else:
                pop=stack.pop()
                exclusive[pop[0]]+=(int(l[2])-latest_time+1)
                latest_time=int(l[2])+1
        return exclusive