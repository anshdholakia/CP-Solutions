class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # build the graph with stop: set of bus
        G = defaultdict(set)
        for i in range(len(routes)):
            for stop in routes[i]:
                G[stop].add(i)
        visited_stop=set({})
        visited_bus=set({})
        queue=collections.deque([(source, 0)]) # stop, length
        length=0
        while queue:
            for _ in range(len(queue)):
                stop, length = queue.popleft()
                if stop==target:
                    return length
                for bus in G[stop]:
                    if bus not in visited_bus:
                        visited_bus.add(bus)
                        for stop in routes[bus]:
                            if stop not in visited_stop:
                                visited_stop.add(stop)
                                queue.append((stop, length+1))
            length+=1
        return -1
