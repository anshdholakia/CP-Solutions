class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        # do union find of the value which are the same
        # then sort the values and assign to them accordingly
        rank=[[0]*len(matrix[0]) for _ in range(len(matrix))]
        parent=[[(i, j) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        def find(n):
            while n!=parent[n[0]][n[1]]:
                parent[n[0]][n[1]]=parent[parent[n[0]][n[1]][0]][parent[n[0]][n[1]][1]]
                n=parent[n[0]][n[1]]
            return n
        def union(a, b):
            p1, p2 = find(a), find(b)
            if rank[p1[0]][p1[1]]>rank[p2[0]][p2[1]]:
                rank[p1[0]][p1[1]]+=rank[p2[0]][p2[1]]
                parent[p2[0]][p2[1]]=p1
            else:
                parent[p1[0]][p1[1]]=p2
                rank[p2[0]][p2[1]]+=rank[p1[0]][p1[1]]
        row_groups=defaultdict(lambda: defaultdict(list))
        col_groups=defaultdict(lambda: defaultdict(list))
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                row_groups[i][matrix[i][j]].append((i, j))
                col_groups[j][matrix[i][j]].append((i, j))
        for row in row_groups:
            for value in row_groups[row]:
                first=row_groups[row][value][0]
                for idx in range(1, len(row_groups[row][value])):
                    union(first, row_groups[row][value][idx])
        for col in col_groups:
            for value in col_groups[col]:
                first=col_groups[col][value][0]
                for idx in range(1, len(col_groups[col][value])):
                    union(first, col_groups[col][value][idx])
                    
        parents=set([find((i, j)) for i in range(len(matrix)) for j in range(len(matrix[0]))])
        value_parent=sorted([(matrix[x][y], x, y) for x, y in parents], key=lambda x: x[0])
        # assigning level is going to be different
        # get the children of the parent
        # check the row and the col levels of each and get level value
        parent_to_child=defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                parent_to_child[find((i, j))].append((i, j))
        row_level=[0]*len(matrix)
        col_level=[0]*len(matrix[0])
        for _, x, y in value_parent:
            level=1
            v = parent_to_child[(x, y)]
            for x, y in v:
                level=max(level, max(row_level[x], col_level[y])+1)
            for x, y in v:
                row_level[x]=level
                col_level[y]=level
                matrix[x][y]=level
        return matrix
            


            