class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        @cache
        def is_prime(n):
            for i in range(2, int(sqrt(n))+1):
                if n%i==0:
                    return False
            return True
        prev=0
        for n in nums:
            upper=n-prev
            p=0
            for p in range(upper-1,1,-1):
                if is_prime(p):
                    break
            if n-p<=prev:
                return False
            prev=n-p
        return True