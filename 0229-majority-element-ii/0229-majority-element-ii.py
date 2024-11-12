class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        SIZE=len(nums)
        THRESHOLD=floor(SIZE/3)
        hashmap={} # contains only two of the most freq elements
        for n in nums:
            hashmap[n]=hashmap.get(n,0)+1
            if len(hashmap)>2:
                for key in hashmap.copy():
                    hashmap[key]-=1
                    if not hashmap[key]:
                        del hashmap[key]
        # verify hashmap vals
        res=[]
        for k in hashmap:
            count=0
            for n in nums:
                if k==n:
                    count+=1
            if count>THRESHOLD:
                res.append(k)
        return res