class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(n, start):
            if not n:
                return True
            for power in range(floor(math.log(n, 3)),start,-1):
                if backtrack(n-3**power, power):
                    return True
            return False
        return backtrack(n, -1)