class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        def dfs(cur_n: int):
            # multiple cur_n by 10 and expand the next level here
            if cur_n>n:
                return []
            result = [cur_n]
            children = []
            for k in range(10):
                children.append(dfs(cur_n*10+k))
            children = sum(children, [])
            return result+children
        result = sum([dfs(x) for x in range(1, 10)], [])
        return result