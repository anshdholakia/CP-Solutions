class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # make a hashmap which stores the value
        # each row are going to be the same if you flip all the letters
        new_matrix=[]
        for row in matrix:
            new_matrix.append(int("".join(map(str, row)),2))
        hashmap=defaultdict(int)
        n=len(matrix[0])
        for val in new_matrix:
            hashmap[val]+=1
            hashmap[val^((1<<n)-1)]+=1
        return max(hashmap.values())