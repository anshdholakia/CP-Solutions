class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res_a, res_b, res_c = -inf, -inf, -inf
        for a, b, c in triplets:
            if a>target[0] or b>target[1] or c>target[2]:
                continue
            res_a, res_b, res_c = max(res_a, a), max(res_b, b), max(res_c, c)
        return [res_a, res_b, res_c]==target