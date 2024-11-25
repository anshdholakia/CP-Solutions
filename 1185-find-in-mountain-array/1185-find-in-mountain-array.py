# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def bin_search(l, r):
            while l<=r:
                m=(l+r)//2
                m_val=mountainArr.get(m)
                if m_val==target:
                    return m
                if m_val<target:
                    l=m+1
                else:
                    r=m-1
        def rev_bin_search(l, r):
            while l<=r:
                m=(l+r)//2
                m_val=mountainArr.get(m)
                if m_val==target:
                    return m
                if m_val>target:
                    l=m+1
                else:
                    r=m-1
                
        # find the peak
        l, r = 0, mountainArr.length()-1
        res=None
        while l<=r:
            m=(l+r)//2
            m_val=mountainArr.get(m)
            m_minus_val=(mountainArr.get(m-1) if m>0 else -inf)
            m_plus_val=(mountainArr.get(m+1) if m<=mountainArr.length()-2 else -inf)
            if m_val>m_minus_val and m_val>m_plus_val:
                #found peak
                if m_val==target:
                    return m
                res=bin_search(0, m-1)
                if res==None:
                    res=rev_bin_search(m+1, mountainArr.length()-1)
                break
            elif m_val<m_plus_val:
                l=m+1
            else:
                r=m-1
        return res if res!=None else -1