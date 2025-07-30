class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls, cows = 0, 0
        secret_d=collections.defaultdict(int)
        guess_d=collections.defaultdict(int)
        for x, y in zip(secret, guess):
            if x==y:
                bulls+=1
            else:
                secret_d[x]+=1
                guess_d[y]+=1
        for k in guess_d:
            cows+=min(secret_d[k], guess_d[k])
        return f"{bulls}A{cows}B"
            