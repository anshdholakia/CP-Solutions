class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # sort it based on time
        splitted_tp = []
        for tp in timePoints:
            t = tp.split(":")
            splitted_tp.append((int(t[0]), int(t[1])))
        splitted_tp.sort()
        splitted_tp.append((splitted_tp[0][0]+24, splitted_tp[0][1]))
        result = float("inf")
        for i in range(len(splitted_tp)-1):
            p1, p2 = splitted_tp[i], splitted_tp[i+1]
            cur_res = (p2[0]-p1[0])*60 + (p2[1]-p1[1])
            result = min(result, cur_res)
        return result
