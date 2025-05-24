class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        # implement prefix sum while doing dfs
        graph=defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        costs=[]
        res=[0, 1]
        last=defaultdict(lambda:-1)
        def dfs(node, cur_sum, prev, left):
            prev_last=last[nums[node]]
            last[nums[node]]=len(costs)
            costs.append(cur_sum)
            if cur_sum-costs[left]>res[0]:
                res[0]=cur_sum-costs[left]
                res[1]=len(costs)-left
            elif cur_sum-costs[left]==res[0]:
                res[1]=min(res[1], len(costs)-left)
            for new_node, new_weight in graph[node]:
                if new_node==prev: continue
                new_left = left
                if last[nums[new_node]]!=-1 and new_left<=last[nums[new_node]]:
                    new_left=last[nums[new_node]]+1
                dfs(new_node, cur_sum+new_weight, node, new_left)
            last[nums[node]]=prev_last
            costs.pop()
        dfs(0, 0, -1, 0)
        return res