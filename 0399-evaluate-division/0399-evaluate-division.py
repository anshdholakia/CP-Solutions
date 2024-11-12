class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # make the relations in a hashmap
        relations=defaultdict(dict)
        for relation, value in zip(equations, values):
            relations[relation[0]][relation[1]]=value
            relations[relation[1]][relation[0]]=1/value
        visited=set({})
        def find(x, target):
            if x not in relations:
                return inf
            if x in visited:
                return inf
            if x==target:
                return 1
            visited.add(x)
            for neighbor, value in relations[x].items():
                if neighbor not in visited:
                    res=find(neighbor, target)*value
                    if res!=inf:
                        visited.remove(x)
                        return res
            visited.remove(x)
            return inf
        res=[]
        for fromm, to in queries:
            curres=find(fromm, to)
            if curres==inf:
                res.append(-1)
            else:
                res.append(curres)
        return res