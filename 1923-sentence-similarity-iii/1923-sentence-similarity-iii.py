class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence2)>len(sentence1):
            sentence1, sentence2 = sentence2, sentence1
        split_1 = sentence1.split(" ")
        split_2 = sentence2.split(" ")
        i, j = 0, 0
        # check for front
        while j<len(split_2) and split_1[i]==split_2[j]:
            i+=1
            j+=1
        if j==len(split_2):
            return True
        # check for back
        i, j = len(split_1)-1, len(split_2)-1
        while j>=0 and split_1[i]==split_2[j]:
            i-=1
            j-=1
        if j==-1:
            return True
        i, j = 0, 0
        while split_1[i]==split_2[j]:
            i+=1
            j+=1
        # check if the len(split_1)-(len(split_2)-j) is equal here
        return "".join(split_1[len(split_1)-(len(split_2)-j):])=="".join(split_2[j:])





