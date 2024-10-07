class Solution:
    def maximumSwap(self, num: int) -> int:
        num=str(num)
        num=[x for x in num]
        preorder = []
        max_num = -1
        for i in range(len(num)-1, -1, -1):
            preorder.append(max_num)
            if int(num[i])>int(num[max_num]):
                max_num = i
        preorder=preorder[::-1]
        for i in range(len(num)-1):
            # if the preorder is greater than current swap
            if int(num[preorder[i]])>int(num[i]):
                num[i], num[preorder[i]] = num[preorder[i]], num[i]
                return int("".join(num))
        return int("".join(num))