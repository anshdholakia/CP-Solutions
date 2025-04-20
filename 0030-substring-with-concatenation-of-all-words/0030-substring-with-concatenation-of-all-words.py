class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        target=collections.Counter(words)
        need=len(target)
        n=len(words[0])
        res=[]
        # important: start the outer loop with only length of word
        for i in range(n):
            start=i
            have=0
            cur_count={}
            for k in range(i, len(s)-n+1, n):
                word=s[k:k+n]
                if word not in target:
                    start=k+n
                    have=0
                    cur_count={}
                    continue
                cur_count[word]=cur_count.get(word,0)+1
                have+=1
                while cur_count[word]>target[word]:
                    cur_count[s[start:start+n]]-=1
                    have-=1
                    start+=n
                if have==len(words):
                    res.append(start)
        return res
