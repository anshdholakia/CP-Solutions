class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
        count = collections.Counter(hand)
        hand.sort()
        for card in hand:
            if count[card]>0:
                for i in range(groupSize):
                    if i+card not in count:
                        return False
                    count[card+i]-=1
            elif count[card]<0:
                return False
        return True
