# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find peak of mountain array
        length=mountainArr.length()
        l, r = 0, length-1
        val=None
        while l<=r:
            m=(l+r)//2
            m_minus=mountainArr.get(m-1) if m-1>=0 else -inf
            m_val=mountainArr.get(m)
            m_plus=mountainArr.get(m+1) if m+1<length else -inf
            if m_minus<m_val and m_val>m_plus:
                val=m_val
                break
            elif m_minus<m_val:
                l=m+1
            else:
                r=m-1
        if val==None or val<target:
            return -1
        if val==target:
            return m
        def binary_search(l, r):
            while l<=r:
                m=(l+r)//2
                m_val=mountainArr.get(m)
                if m_val==target:
                    return m
                elif m_val<target:
                    l=m+1
                else:
                    r=m-1
            return None
        def rev_binary_search(l, r):
            while l<=r:
                m=(l+r)//2
                m_val=mountainArr.get(m)
                if m_val==target:
                    return m
                elif m_val>target:
                    l=m+1
                else:
                    r=m-1
            return None
        # search in the 0..m-1 array first
        first=binary_search(0, m-1)
        if first!=None:
            return first
        # search in the m+1..length array second
        second=rev_binary_search(m+1, mountainArr.length()-1)
        if second!=None:
            return second
        return -1

