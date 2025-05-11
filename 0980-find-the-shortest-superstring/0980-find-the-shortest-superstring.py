class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        # use bitmask and dp
        def adjacent():
            # build the adj array which stores the non-overlapping parts
            adj=[[0]*len(words) for _ in range(len(words))]
            for i in range(len(words)):
                for j in range(len(words)):
                    if i!=j:
                        x, y = words[i], words[j]
                        max_overlap=0
                        for k in range(1, min(len(x), len(y))+1):
                            if x[-k:]==y[:k]:
                                max_overlap=k
                        adj[i][j]=y[max_overlap:]
            return adj
        def dp(chosen, cur):
            if chosen==(1<<len(words))-1: return ""
            if (chosen, cur) in memo:
                return memo[(chosen, cur)]
            res='a'*241
            for i in range(len(words)):
                if ((1<<i) & chosen)==0:
                    cur_res=adj[cur][i]+dp(chosen|(1<<i), i)
                    if len(cur_res)<len(res):
                        res=cur_res
            memo[(chosen, cur)]=res
            return res
        adj=adjacent()
        res='a'*241
        memo={}
        for i in range(len(words)):
            cur=words[i]+dp(1<<i, i)
            if len(cur)<len(res):
                res=cur
        return res