class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        array=[(c, r) for c, r in zip(chargeTimes, runningCosts)]
        def check(k):
            if k==0:
                return True
            # use monotonic queue to track max
            queue=collections.deque([])
            running_sum=sum([x[1] for x in array[:k]])
            for i in range(k):
                while queue and queue[-1][0]<array[i][0]:
                    queue.pop()
                queue.append((*array[i], i))
            if queue[0][0]+k*running_sum<=budget:
                return True
            l=0
            for i in range(k, len(array)):
                running_sum-=array[l][1]
                running_sum+=array[i][1]
                l+=1
                while queue and queue[0][-1]<l:
                    queue.popleft()
                while queue and queue[-1][0]<array[i][0]:
                    queue.pop()
                queue.append((*array[i], i))
                if queue[0][0]+k*running_sum<=budget:
                    return True
            return False
        l, r = 0, len(array)
        res=0
        while l<=r:
            m=(l+r)//2
            if check(m):
                res=m
                l=m+1
            else:
                r=m-1
        return res