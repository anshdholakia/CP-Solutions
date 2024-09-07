class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        queue = collections.deque(strs)
        while len(queue)>1:
            pop1, pop2 = queue.popleft(), queue.popleft()
            ptr1, ptr2 = 0, 0
            while ptr1<len(pop1) and ptr2<len(pop2) and pop1[ptr1]==pop2[ptr2]:
                ptr1+=1
                ptr2+=1
            queue.append(pop1[:ptr1])
        return queue[0]
