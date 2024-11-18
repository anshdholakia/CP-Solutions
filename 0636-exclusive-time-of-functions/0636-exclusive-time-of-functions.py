class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack=[]
        latest_time=0
        exclusive=[0]*n
        for log in logs:
            ID, OP, TIME = log.split(":")
            if OP=="start":
                if stack:
                    exclusive[stack[-1][0]]+=(int(TIME)-latest_time)
                stack.append((int(ID), int(TIME)))
                latest_time=int(TIME)
            else:
                stack.pop()
                exclusive[int(ID)]+=(int(TIME)-latest_time+1)
                latest_time=int(TIME)+1
        return exclusive
