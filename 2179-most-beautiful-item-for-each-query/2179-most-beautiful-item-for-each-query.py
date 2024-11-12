class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: (x[0], x[1]))
        max_beauty=-inf
        for i in range(len(items)):
            max_beauty=max(max_beauty, items[i][1])
            items[i][1]=max_beauty
        res=[]
        for q in queries:
            l, r = 0, len(items)-1
            cur_res=-inf
            while l<=r:
                m=(l+r)//2
                if items[m][0]<=q:
                    cur_res=max(cur_res, items[m][1])
                    l=m+1
                else:
                    r=m-1
            if cur_res!=-inf:
                res.append(cur_res)
            else:
                res.append(0)
        return res