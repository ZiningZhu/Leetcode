class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """

        stop_bus_dict = {}
        for b in range(len(routes)):
            route = routes[b]
            for stop in route:
                if stop in stop_bus_dict:
                    stop_bus_dict[stop].append(b)
                else:
                    stop_bus_dict[stop] = [b]

        # Now we can just BFS
        # Treat each bus as a node
        if S == T:
            return 0
        if S not in stop_bus_dict:
            return -1
        queue = [(b, 1) for b in stop_bus_dict[S]]
        visited = [False] * len(routes)
        while len(queue) > 0:
            curr_bus, bus_taken = queue.pop(0)
            if visited[curr_bus]:
                continue
            else:
                visited[curr_bus] = True
            if T in routes[curr_bus]:
                return bus_taken
            connected_buses = []
            for stop in routes[curr_bus]:
                for b in stop_bus_dict[stop]:
                    if b not in connected_buses:
                        connected_buses.append(b)
            for b in connected_buses:
                if not visited[b]:
                    queue.append((b, bus_taken+1))
        return -1
