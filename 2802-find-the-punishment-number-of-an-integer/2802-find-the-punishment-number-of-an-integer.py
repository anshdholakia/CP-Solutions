class Solution:
    def punishmentNumber(self, n: int) -> int:
        total=0
        def check(num, target, cur_sum):
            if not num:
                return cur_sum==target
            if cur_sum>target:
                return False
            for i in range(1, len(num)+1):
                if check(num[i:], target, cur_sum+int(num[:i])):
                    return True
            return False
        for i in range(1, n+1):
            if check(str(i*i), i, 0):
                total+=i*i
        return total