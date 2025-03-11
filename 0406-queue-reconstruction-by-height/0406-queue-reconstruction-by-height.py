class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # sort the array based on comparator
        def cmp(a, b):
            if a[0]<b[0]:
                return -1
            elif a[0]==b[0]:
                return -1 if a[1]<b[1] else 1
            return 1
        people.sort(key=cmp_to_key(cmp))
        # for each of the element place it in the array
        res=[None]*len(people)
        for h, p in people:
            cnt=0
            for i in range(len(res)):
                if res[i]==None and cnt==p:
                    res[i]=[h,p]
                    break 
                elif res[i]==None or res[i][0]>=h:
                    cnt+=1
        return res
