class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_n = mean*(len(rolls)+n)-sum(rolls)
        if sum_n>6*n or sum_n<n:
            return []
        result = [1]*n
        remaining = sum_n-n
        for i in range(len(result)):
            need = min(5, remaining)
            result[i]+=need
            remaining-=need
        return result