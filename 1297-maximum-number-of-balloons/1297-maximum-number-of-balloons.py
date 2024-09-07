class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = collections.Counter("balloon")
        text_count = collections.Counter(text)
        text_count = {k: v for k, v in text_count.items() if k in target and target[k]<=text_count[k]}
        if len(text_count)!=len(target):
            return 0
        result = 0
        while True:
            for c in text_count:
                text_count[c]-=target[c]
                if text_count[c]<0:
                    del text_count[c]
                    break
            else:
                result+=1
            if len(text_count)<len(target):
                break
        return result