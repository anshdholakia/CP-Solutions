class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k==1:
            return max(arr[0], arr[1])
        # brain teaser part
        if k>=len(arr):
            return max(arr)
        current_winner = arr[0]
        current_winner_cnt=0
        for x in arr[1:]:
            if x<current_winner:
                current_winner_cnt+=1
            else:
                current_winner=x
                current_winner_cnt=1
            if current_winner_cnt==k:
                return current_winner
        return current_winner
