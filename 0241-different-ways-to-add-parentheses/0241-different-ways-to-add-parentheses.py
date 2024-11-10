class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operator={'+':lambda n1,n2:n1+n2, '-':lambda n1,n2:n1-n2, '*':lambda n1,n2:n1*n2}
        def backtrack(left, right):
            res=[]
            for i in range(left, right+1):
                if expression[i] in '*+-':
                    nums1=backtrack(left, i-1)
                    nums2=backtrack(i+1, right)
                    for n1 in nums1:
                        for n2 in nums2:
                            res.append(operator[expression[i]](n1, n2))
            if not res:
                return [int(expression[left:right+1])]
            return res
        return backtrack(0, len(expression)-1)