class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xors = {-1:0}
        cur_xor = 0
        for i in range(len(arr)):
            cur_xor^=arr[i]
            prefix_xors[i]=cur_xor
        answers = []
        for s, e in queries:
            # c = a^b
            # a = c^b or b = c^a
            answers.append(prefix_xors[e]^prefix_xors[s-1])
        return answers



        