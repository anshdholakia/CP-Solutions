class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result = [-float("inf"), -float("inf"), -float("inf")]
        for a, b, c in triplets:
            if a>target[0] or b>target[1] or c>target[2]:
                continue
            result = [max(result[0], a), max(result[1], b), max(result[2], c)]
        return result==target
