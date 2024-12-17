class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        heap=[(-ord(c), cnt) for c, cnt in collections.Counter(s).items()]
        heapq.heapify(heap)
        res=""
        while heap:
            ch, cnt = heapq.heappop(heap)
            used=min(cnt, repeatLimit)
            cnt-=used
            res+=chr(-ch)*used
            if cnt>0:
                # check the next element and always use one from that
                if not heap:
                    break
                next_ch, next_cnt = heapq.heappop(heap)
                res+=chr(-next_ch)
                next_cnt-=1
                if next_cnt:
                    heapq.heappush(heap, (next_ch, next_cnt))
                heapq.heappush(heap, (ch, cnt))
        return res