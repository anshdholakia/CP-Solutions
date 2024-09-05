class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        G = defaultdict(set)
        email_to_name = defaultdict(str)
        for acc in accounts:
            name = acc[0]
            email_to_name[acc[1]] = name
            G[acc[1]]
            for email1, email2 in zip(acc[1:], acc[2:]):
                email_to_name[email1] = name
                email_to_name[email2] = name
                G[email1].add(email2)
                G[email2].add(email1)
        def bfs(email_name):
            queue = collections.deque([email_name])
            visited.add(email_name)
            cur_result = [email_name]
            while queue:
                popped = queue.popleft()
                for n in G[popped]:
                    if n in visited:
                        continue
                    queue.append(n)
                    visited.add(n)
                    cur_result.append(n)
            return cur_result
        visited = set({})
        result = []
        for email in G:
            if email in visited:
                continue
            bfs_result = bfs(email)
            result.append([email_to_name[bfs_result[0]]] + sorted(bfs_result))
        return result
        

            

